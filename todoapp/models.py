from django.db import models

# Create your models here.

class Todo(models.Model):
    text =  models.CharField(max_length=1000)
    date =  models.DateField(auto_now_add=True)
    class Meta:
        ordering = ['id']
    def __str__(self):
        return self.text
