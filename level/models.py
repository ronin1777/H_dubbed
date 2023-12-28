from django.db import models


class Level(models.Model):
    level_numb = models.IntegerField(null=True, blank=True)
    required_points = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.level_numb)



