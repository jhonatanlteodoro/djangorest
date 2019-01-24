from datetime import datetime
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    create_on = models.DateTimeField(default=datetime.now)

    CATEGORIES = (
        ('notebooks', 'Notebooks'),
        ('eletrodomesticos', 'Eletrodomésticos'),
        ('moveis', 'Móveis'),
        ('smartphone', 'Smartphone')
    )
    category = models.CharField(max_length=16, choices=CATEGORIES)
