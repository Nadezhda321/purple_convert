from django.db import models

class Foto(models.Model):
    img = models.ImageField('Изображение', upload_to='main/photos')

    def __str__(self):
        return self.img



    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Foto'


class FileServ:
    pass