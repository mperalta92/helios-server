from django.db import models
from helios.models import Voter
from signbook.models.merkle_tree import MerkleTree


class Signature(models.Model):
    # Voter tiene usuario y hash del voto
    voter = models.ForeignKey(Voter)
    # Esto es un hash
    signature = models.CharField(max_length=255)
    vector = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    root = models.ForeignKey(MerkleTree)

    def save_vector(self, vector):
        self.vector = ",".join(vector)

    @property
    def get_vector(self):
        return self.vector.split(',')

    @property
    def vote_hash(self):
        return self.voter.vote_hash
