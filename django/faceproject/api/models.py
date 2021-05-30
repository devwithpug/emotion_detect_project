from django.db import models
from .ml import face


class Face(models.Model):
    content = models.TextField()

    @property
    def result(self):
        return face.do(self.content)

    def __str__(self):
        return '{}'.format(self.result)
