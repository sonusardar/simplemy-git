from django.db import models

# Create your models here.

class DropBox(models.Model):
    Fileid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    dbfile = models.FileField(upload_to='')