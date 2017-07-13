import math
from Nodo import *
from MerkleVerifier import *


class MerkleTree:
    # h = tree's height. Leaves = 2^h
    # otsScheme = a list of containing the selected one-time-signature scheme's algorithms
    #   It's in this format: [K,S,V]
    # g = hashing function
    def __init__(self, h, otsScheme , g):
        self.pk = ''
        self.sk = []
        self.otsScheme = otsScheme
        self.hash = g
        self.current_key_index = 0
        self.height = h
        self.db_ref = None
        #Merkle Tree Generation:
        stack = []
        for i in range(int(math.pow(2,h))):
            currentPair = otsScheme[0]()
            node1 = Nodo(g(currentPair[1]))
            self.sk.append(currentPair)
            while stack and (node1.getAltura() == stack[len(stack) - 1].getAltura()):
                node2 = stack.pop()
                val_node = g(node2.getElement()+node1.getElement())
                node1 = Nodo(val_node, node2, node1)
            stack.append(node1)
        self.pk = stack.pop()

        #Initialiaze verifier
        self.Verifier = MerkleVerifier()
        self.Verifier.pk = self.pk
        self.Verifier.hash =  g
        self.Verifier.ver_ots = otsScheme[2]

    def get_pk(self):
        return self.pk

    def sign(self, m):
        i = self.current_key_index
        if i >= math.pow(2,self.height):
            raise ValueError('You have ran out of key pairs')
        d = self.hash(m)
        s_ots = self.otsScheme[1](d, self.sk[i][0])
        auth_path = self.tracking_path(self.height, self.pk, i)
        # [Verification Key_i, authentification path for said key, ots's signature, current key pair index]
        S_m = [self.sk[i][1], auth_path, s_ots, i]
        self.current_key_index += 1
        return S_m

    def tracking_path(self, h, root, index):
        r = []
        if h == 0:
            return r
        if(index < math.pow(2,h-1)):
            r.append(root.getDer().getElement())
            r = r + self.tracking_path((h - 1), root.getIzq(), index)
        else:
            r.append(root.getIzq().getElement())
            r = r + self.tracking_path((h - 1), root.getDer(), index - math.pow(2, h - 1))
        return r

    def get_verifier(self):
        return self.Verifier;

