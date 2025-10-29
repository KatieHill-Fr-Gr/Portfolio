from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=100)
    icon = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name
