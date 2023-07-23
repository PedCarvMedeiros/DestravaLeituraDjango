from django.db import models

# Create your models here.
class LivroInfo(models.Model):

    nome = models.CharField(max_length=264)
    autor = models.CharField(max_length=264)
    genero = models.CharField(max_length=264)
    xerox = models.CharField(max_length=264)
    emprestado = models.CharField(max_length=264)
    foto = models.ImageField(null=True, blank=True, upload_to="images/")
    
    def foto_url(self):
        if self.foto:
            return self.foto.url
        else:
            return '/static/images/book.jpg'

    



