from django.db import models
from django.contrib import admin

from groceries import SECTIONS_IN_SHOP
from groceries.admin import ItemAdmin


class Item(models.Model):
    name = models.CharField(max_length=256)
    photo = models.ImageField(null=True, blank=True)
    section = models.CharField(max_length=2, choices=SECTIONS_IN_SHOP)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"groceries item: [{self.name}]({self.section})"


admin.site.register(Item, ItemAdmin)
