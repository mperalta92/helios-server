from MerkleTree import MerkleTree
from OtsScheme import OtsScheme

new_ots = OtsScheme()
# Generar un MerkleTree
Merky = MerkleTree(4,[new_ots.K, new_ots.S, new_ots.V], new_ots.my_hash)
# Recuperar su raiz
root = Merky.get_pk()

# Funcion para imprimir (de forma muy simplifista) el arbol
def printTree(roo):
    if roo.getIzq() != None: printTree(roo.getIzq())
    print "(" + str(roo.getAltura()) + " - " + roo.getElement() + ") "
    if roo.getDer() != None: printTree(roo.getDer())

print Merky.sk
printTree(root)
print "\n\n"
# Obtener verificador (el firmador es parte del arbol, el verificador es un objeto aparte)
very = Merky.get_verifier()
mens = "mensaje"
#Imprimir firma e imprimir si se verifica
for i in range(16):
    firma = Merky.sign(mens + str(i))
    print firma
    print very.verify("mensaje" + str(i), firma)

print "\nDone"
