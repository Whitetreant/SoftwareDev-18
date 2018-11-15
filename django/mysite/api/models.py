from django.db import models

class Note(models.Model):
    Value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class temp(models.Model):
    Value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add = True)

def __str__(self):
    return '%s %s' % (self.Value,self.created_at)

# Create your models here.
