from django.db import models
from signbook.models.Node import Node
from helios.models import Voter
from datetime import datetime


class MerkleTree(models.Model):
    root_value = models.CharField(max_length=255, null=True, blank=True)
    root = models.ForeignKey(Node)
    machine = models.CharField(max_length=255)
    create_at = models.DateTimeField(default=datetime.now())
    voters = models.ManyToManyField(Voter)
    secret_value_to_verifier = models.CharField(max_length=255)

