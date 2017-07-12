# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helios', '0003_auto_20160507_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='MerkleTree',
            fields=[
                ('root', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('machine', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField()),
                ('voters', models.ManyToManyField(to='helios.Voter')),
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
    ]
