import math


class MerkleVerifier:
    # Instance variables are supposed to be directly initialized by the MerkleTree class
    def __init__(self):
        self.hash = None
        self.ver_ots = None
        self.pk = None

    def verify(self, message, signature):
        # stage 1: Verify the message using the OTS
        d = self.hash(message)
        y_i = signature[0]
        s_ots = signature[2]
        i = signature[3]
        if not self.ver_ots(d, s_ots, y_i):
            return False
        # stage 2: Authenticate the key y_i
        auth_path = signature[1];
        h = self.hash(y_i)
        for j in range(len(auth_path)):
            if int(i/math.pow(2,j))%2:
                h = self.hash(auth_path[len(auth_path)-1-j] + h)
            else:
                h = self.hash(h+ auth_path[len(auth_path) - 1 - j])
        return h == self.pk.getElement()
