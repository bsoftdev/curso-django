from django.db import models

# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    conteudo = models.TextField(verbose_name='Conteudo do Post')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Postado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado em')


    class Meta:
        ordering = ['created_at']
        verbose_name = 'Post'

    def __str__(self):
        return f'{self.titulo}'


    