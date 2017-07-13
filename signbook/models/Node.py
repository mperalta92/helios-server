from django.db import models


class Node(models.Model):
    high = models.IntegerField()
    value = models.CharField(max_length=255)
    left_child = models.ForeignKey('self', related_name='left_')
    right_child = models.ForeignKey('self', related_name='right_')
