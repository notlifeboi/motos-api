from django.db import models


class Moto(models.Model):
    id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length = 30, blank = False, null = False)
    trademark = models.CharField(max_length = 30, blank = False, null = False)
    model = models.CharField(max_length = 30, blank= False, null =  False,)
    price = models.IntegerField()
    # Todas las imagenes que se guarden, irán a la carpeta de imagenes
    image = models.ImageField(upload_to='images', blank = False, null = False)
    supplier = models.CharField(max_length = 60, blank = False, null = False)

def __str__(self):
    return self.reference
