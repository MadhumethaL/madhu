from django.db import models

class Usersdata(models.Model):
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    def __str__(self):
        return f"{self.Username}"   


class Score(models.Model):
    Username=models.CharField(max_length=20)
    points=models.IntegerField(("points"))
    def __str__(self):
        return self.Username