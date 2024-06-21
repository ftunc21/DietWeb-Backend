from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    detailed_description = models.TextField(null=True, blank=True)  # Yeni alan
    time = models.PositiveIntegerField()  # Dakika cinsinden pişirme süresi
    difficulty = models.CharField(max_length=50)
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)  # Opsiyonel resim alanı

    def __str__(self):
        return self.title
