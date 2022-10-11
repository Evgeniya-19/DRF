from django.db import models

class Manager(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    user_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
