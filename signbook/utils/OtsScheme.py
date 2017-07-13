from Crypto.Hash import SHA256
from Crypto.Random.random import getrandbits


class OtsScheme:

    NUMBER_OF_RANDOM_BITS = 256
    SECRET_KEY = getrandbits(NUMBER_OF_RANDOM_BITS)

    @classmethod
    def my_hash(cls, m):
        return SHA256.new(str(m)).hexdigest()

    @classmethod
    def K(cls):
        rand = getrandbits(cls.NUMBER_OF_RANDOM_BITS)
        y = cls.my_hash(rand)
        x = cls.my_hash(str(cls.SECRET_KEY) + y)
        return [x, y]

    @classmethod
    def S(cls, d, x):
        return cls.my_hash(d + "|C:|" + x)

    @classmethod
    def V(cls, d, sig, y):
        x = cls.my_hash(str(cls.SECRET_KEY) + y)
        return sig == cls.my_hash(d + "|C:|" + x)

