from signbook.models import Node
from Crypto.Hash import SHA256
from signbook.utils import MerkleVerifier
from signbook.utils import Nodo


def save_merkle_tree(self, merkle_node):
    new_node = Node()
    new_node.high = merkle_node.altura
    new_node.value = merkle_node.element
    if merkle_node.izq is not None and merkle_node.der is not None:
        new_node.left_child = save_merkle_tree(merkle_node.izq)
        new_node.right_child = save_merkle_tree(merkle_node.der)
    new_node.save()
    return new_node


def my_hash(m):
    return SHA256.new(str(m)).hexdigest()


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

