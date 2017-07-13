from MerkleTree import MerkleTree
from OtsScheme import OtsScheme
from signbook.utils.functions import my_hash
from signbook.utils.functions import save_merkle_tree
from signbook.models import MerkleTree

merky = None
db_merky = None
verifier = None

#inicia la votación, y hay que generar el primer merkle tree para poder firmar
def new_merkle_tree():

    #generamos el otsScheme del merkle
    new_ots = OtsScheme()
    # creamos un merkle de altura 2 (eso implica que solo puede firmar 4 votos)
    merky = MerkleTree(2,[new_ots.K, new_ots.S, new_ots.V], my_hash)

    # Recuperar su raiz
    root = merky.get_pk()

    # creamos los nodos del merkle tree en la base de datos
    db_root = save_merkle_tree(root)
    # creamos un merkle en la db
    db_merky = MerkleTree(root_value=root.element)
    db_merky.root = db_root
    db_merky.machine = "MACHINE_01"
    db_merky.secret_value_to_verifier = str(new_ots.SECRET_KEY)

    # obtenemos objeto verificador de firmas
    verifier = merky.get_verifier()


# firmar cada mensaje
def firmar(mensaje, voter):
    try:
        firma = merky.sign(mensaje)
    except:
        #significa que ya no puedo seguir firmando, y tengo que crear un nuevo merkle-Tree
        new_merkle_tree()
        firma = merky.sign(mensaje)

    if db_merky.voters is None:
        db_merky.voters = str(voter.uuid)
    else:
        db_merky.voters += "||" + str(voter.uuid)
    str_firma = ""
    i = 0
    while i < firma.length :
        if i !=0:
            str_firma += "||" + str(firma[i])
        else:
            str_firma = "" + str(firma[i])
    return [firma, str_firma]


