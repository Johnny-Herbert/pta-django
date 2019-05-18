from django.db import models

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length = 100, null = False, blank = False, verbose_name = "Titulo") #nao pode ser nulo e vazio
    text = models.TextField(null = False, blank = False) #nao pode ser nulo e vazio
    image = models.ImageField('Imagem', upload_to = 'institute/', null = False, blank = False)
    created_date = models.DateTimeField(auto_now_add=True)
    upudated_date = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'

    def __str__(self):
       return self.title
