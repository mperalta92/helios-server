import settings
from signbook.models import MerkleTree
from signbook.models.Node import Node
from Crypto.Hash import SHA256
from signbook.utils import MerkleVerifier
from signbook.utils import Nodo
from signbook.utils.MerkleTree import MerkleTree as MerkleTreeCustom
from signbook.utils.OtsScheme import OtsScheme


def my_hash(m):
    return SHA256.new(str(m)).hexdigest()


def new_merkle_tree():

    #generamos el otsScheme del merkle
    new_ots = OtsScheme()
    # creamos un merkle de altura 2 (eso implica que solo puede firmar 4 votos)
    settings.MERKY = MerkleTreeCustom(2,[new_ots.K, new_ots.S, new_ots.V], my_hash)

    # Recuperar su raiz
    root = settings.MERKY.get_pk()

    # creamos los nodos del merkle tree en la base de datos
    db_root = save_merkle_tree(root)
    # creamos un merkle en la db
    settings.MERKY.db_ref = MerkleTree(root_value=root.element)
    settings.MERKY.db_ref.root = db_root
    settings.MERKY.db_ref.machine = "MACHINE_01"
    settings.MERKY.db_ref.secret_value_to_verifier = str(new_ots.SECRET_KEY)

    # obtenemos objeto verificador de firmas
    verifier = settings.MERKY.get_verifier()

# firmar cada mensaje
def firmar(mensaje, voter):
    try:
        firma = settings.MERKY.sign(mensaje)
    except:
        #significa que ya no puedo seguir firmando, y tengo que crear un nuevo merkle-Tree
        new_merkle_tree()
        firma = settings.MERKY.sign(mensaje)

    if settings.MERKY.db_ref.voters is None:
        settings.MERKY.db_ref.voters = str(voter.uuid)
    else:
        settings.MERKY.db_ref.voters += "||" + str(voter.uuid)
    str_firma = ""
    i = 0
    while i < firma.length :
        if i !=0:
            str_firma += "||" + str(firma[i])
        else:
            str_firma = "" + str(firma[i])
    return [firma, str_firma]


def save_merkle_tree(merkle_node):
    new_node = Node()
    new_node.high = merkle_node.altura
    new_node.value = merkle_node.element
    if merkle_node.izq is not None and merkle_node.der is not None:
        new_node.left_child = save_merkle_tree(merkle_node.izq)
        new_node.right_child = save_merkle_tree(merkle_node.der)
    new_node.save()
    return new_node


def make_nodo(node):
    if node is None:
        return None
    res = Nodo(node.value)
    res.altura = node.high
    res.izq = make_nodo(node.left_child)
    res.der = make_nodo(node.right_child)
    return res


def get_merkle_tree(root_value):
    root_node = Node.objects(value=root_value).first()
    root = make_nodo(root_node)
    return root


def make_verifier(root_value, secret_value):
    verifier = MerkleVerifier()
    verifier.pk = get_merkle_tree(root_value)
    verifier.hash = my_hash
    verifier.ver_ots = lambda d, sig, y:  sig == my_hash(d + "|C:|" + my_hash(str(secret_value) + y))
    return verifier

