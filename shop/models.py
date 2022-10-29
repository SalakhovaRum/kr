from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class CalcHistory(models.Model):
    ibd = models.CharField(max_length=200)
    val1 = models.CharField(max_length=50)
    val2 = models.CharField(max_length=50)
    operator = models.DateTimeField('Дата публикации')
    created_at = models.DateTimeField(auto_now_add=True)
    result = models.TextField()




# Create your models here.
