from django.db import models


# Create your models here.
class CalcHistory(models.Model):
    #ibd = models.CharField(max_length=200)
    val1 = models.IntegerField()
    val2 = models.IntegerField()
    operator = models.DateTimeField('Дата публикации')
    created_at = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=100, null=True, blank=True)
