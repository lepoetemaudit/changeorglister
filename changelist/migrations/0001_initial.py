# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Petition',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('petition_id', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('country', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=150, null=True)),
                ('name', models.CharField(max_length=150)),
                ('signed_up', models.DateTimeField(null=True)),
                ('petition', models.ForeignKey(to='changelist.Petition')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
