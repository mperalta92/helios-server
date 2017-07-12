from django.db import models

from helios.models import Voter


class MerkleTree(models.Model):
    root = models.CharField(max_length=255, primary_key=True)
    machine = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    voters = models.ManyToManyField(Voter)
