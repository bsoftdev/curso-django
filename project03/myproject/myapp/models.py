from django.db import models

# Create your models here.
    
class Client(models.Model):
    name_client = models.CharField(max_length=100 , blank=True, null=True)
    email = models.EmailField(max_length=100,  blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']


    def __str__(self):
        return f'{self.name_client}'