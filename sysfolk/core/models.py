from django.db import models


class Person(models.Model):
    name = models.CharField('nome', max_length=255)

    def __str__(self):
        return self.name
