from django.db import models


class Node(models.Model):
    high = models.IntegerField()
    value = models.CharField(max_length=255)
    left_child = models.ForeignKey("Node")
    right_child = models.ForeignKey("Node")
