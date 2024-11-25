from django.db import models
from django.contrib.auth.models import User

class Code(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    question =  models.TextField(max_length=1000)
    answer = models.TextField(max_length=5000)
    language =  models.TextField(max_length=100)    
    
    def __str__(self):
        return self.question