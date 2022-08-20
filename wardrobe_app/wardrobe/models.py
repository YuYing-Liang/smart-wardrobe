from django.db import models

class ClothingItem(models.Model):
    name = models.CharField(max_length=255, null=False)
    type = models.CharField(max_length=255, null=False)
    color = models.CharField(max_length=255, null=False)
    season = models.CharField(max_length=255, null=False)

    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.name
