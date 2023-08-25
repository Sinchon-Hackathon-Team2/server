from django.db import models

class Univ(models.Model):
    univName = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.univName

class User(models.Model):
    nickName = models.CharField(max_length=50, unique=True)
    email = models.EmailField(default='', max_length=100, null=False, unique=True)
    univ_id = models.ForeignKey(Univ, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickName

