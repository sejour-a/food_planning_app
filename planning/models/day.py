from django.db import models
from django.contrib import admin

from planning.admin import DayAdmin


class Day(models.Model):
    date = models.DateField(null=True, blank=True)
    week = models.ForeignKey("planning.week", on_delete=models.CASCADE)
    lunch = models.ForeignKey("planning.dish", on_delete=models.CASCADE, related_name="lunch_on_days_set")
    dinner = models.ForeignKey("planning.dish", on_delete=models.CASCADE, related_name="dinner_on_days_set")

    def __str__(self):
        return str(self.date)


admin.site.register(Day, DayAdmin)