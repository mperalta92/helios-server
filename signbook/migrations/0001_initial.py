# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('helios', '0003_auto_20160507_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='MerkleTree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('root_value', models.CharField(max_length=255, null=True, blank=True)),
                ('machine', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(default=datetime.datetime(2017, 7, 13, 3, 53, 5, 741002))),
                ('secret_value_to_verifier', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('high', models.IntegerField()),
                ('value', models.CharField(max_length=255)),
                ('left_child', models.ForeignKey(related_name='left_', to='signbook.Node')),
                ('right_child', models.ForeignKey(related_name='right_', to='signbook.Node')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('signature', models.CharField(max_length=255)),
                ('vector', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('root', models.ForeignKey(to='signbook.MerkleTree')),
                ('voter', models.ForeignKey(to='helios.Voter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='merkletree',
            name='root',
            field=models.ForeignKey(to='signbook.Node'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='merkletree',
            name='voters',
            field=models.ManyToManyField(to='helios.Voter'),
            preserve_default=True,
        ),
    ]
