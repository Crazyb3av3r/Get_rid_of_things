from django.db import models

# Create your models here.
TYPE_CHOICES = (
    (1, 'fundacja'),
    (2, 'organizacja pozarządowa'),
    (3, 'zbiórka lokalna')
)


class Category(models.Model):
    name = models.CharField(max_length=64)


class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    type = models.IntegerField(choices=TYPE_CHOICES, default=1)
    categories = models.ManyToManyField(Category, related_name='category')
    