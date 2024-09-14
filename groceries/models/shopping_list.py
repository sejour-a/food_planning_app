from django.db import models
from django.contrib import admin

from groceries.admin import ShoppingListAdmin


class ShoppingList(models.Model):
    creation_date = models.DateField(auto_now=True)
    completion_date = models.DateField(blank=True, null=True)
    items = models.ManyToManyField("groceries.item", blank=True)
    target_week = models.ForeignKey("planning.week", on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        _week_string = ""
        if self.target_week:
            _week_string = f" for {self.target_week}"

        _completion_string = ""
        if self.completion_date:
            _completion_string = f" (completed {self.completion_date})"


        return f"Shopping List{_week_string}{_completion_string}"

    def __repr__(self):
        return str(self)


admin.site.register(ShoppingList, ShoppingListAdmin)
