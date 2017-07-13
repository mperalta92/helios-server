from Crypto.Random.random import getrandbits
from signbook.utils.functions import my_hash


class OtsScheme:

    NUMBER_OF_RANDOM_BITS = 256
    SECRET_KEY = getrandbits(NUMBER_OF_RANDOM_BITS)

    @classmethod
    def K(cls):
        rand = getrandbits(cls.NUMBER_OF_RANDOM_BITS)
        y = my_hash(rand)
        x = my_hash(str(cls.SECRET_KEY) + y)
        return [x, y]

    @classmethod
    def S(cls, d, x):
        return my_hash(d + "|C:|" + x)

    @classmethod
    def V(cls, d, sig, y):
        x = my_hash(str(cls.SECRET_KEY) + y)
        return sig == my_hash(d + "|C:|" + x)

