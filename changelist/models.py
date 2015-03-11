from django.db import models

class Petition(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    petition_id = models.IntegerField()


class Signature(models.Model):
    petition = models.ForeignKey(to=Petition)
    country = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=150, null=True)
    name = models.CharField(max_length=150)
    signed_up = models.DateTimeField(null=True)