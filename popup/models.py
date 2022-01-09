from django.db import models

class Dropdown(models.Model):
    value = models.IntegerField()

    def __str__(self) -> str:
        return str(self.value)
