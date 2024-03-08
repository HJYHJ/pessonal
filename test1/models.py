from django.db import models

# Create your models here.
#创建表
class girl(models.Model):
    id   = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    hair = models.CharField(max_length=20)
    eyes = models.CharField(max_length=20)
    form = models.CharField(max_length=20)
    born = models.CharField(max_length=20)
    habbits = models.TextField(max_length=254)

class otBoys(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
class otBoysInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.ForeignKey(otBoys,on_delete=models.CASCADE)
    views = models.ManyToManyField('ImageModel',related_name='otboys_info')
    describe = models.TextField(max_length=254)
    showtime = models.CharField(max_length=20)
    habbits = models.TextField(max_length=254)
    fromWhere = models.CharField(max_length=20)
    skills = models.CharField(max_length=20)
    special = models.CharField(max_length=20)
    BGMlinks = models.CharField(max_length=20)
class ImageModel(models.Model):
    image= models.ImageField(upload_to='image/')