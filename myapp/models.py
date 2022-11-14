from django.db import models

# Create your models here.
class RegisteredClient(models.Model):
    epic_no = models.CharField(max_length=20,primary_key=True)
    st_name = models.CharField(max_length=30)
    st_code = models.CharField(max_length=4)
    dist_name = models.CharField(max_length=30)
    dist_no = models.CharField(max_length=4)
    ac_name = models.CharField(max_length=30)
    ac_no = models.CharField(max_length=4)
    part_name = models.CharField(max_length=30)
    part_no = models.CharField(max_length=4)
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=4)
    gender = models.CharField(max_length=3)
    rln_name = models.CharField(max_length=50)
    rln_type = models.CharField(max_length=3)


class ElectoralDataTable(models.Model):
    epic_no = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    age = models.CharField(max_length=5)
    gender = models.CharField(max_length=3)
    house_no = models.CharField(max_length=100)