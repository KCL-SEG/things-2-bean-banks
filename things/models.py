from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Thing(models.Model):
    name = models.CharField(verbose_name='Name', max_length=35, unique=True)
    description = models.CharField(verbose_name='Description', max_length=120, blank=True)
    quantity = models.IntegerField(verbose_name='Quantity',
        validators=[MinValueValidator(0),MaxValueValidator(50)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
