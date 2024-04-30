from django.db import models

#id, nome,
class Client(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    cnpj = models.CharField(max_length=20, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)

class Vehicle(models.Model):

    id = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=300, null=False, blank=False)
    model = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'core_vehicle'

class Condutor(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    cpf = models.CharField(max_length=200, blank=False, null=False)
    age = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)