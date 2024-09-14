from django.db import models
from django.contrib import admin

from planning.admin import WeekAdmin


class Week(models.Model):
    monday_date = models.DateField(null=True, blank=True, unique=True)

    def __str__(self):
        _iso_date = self.monday_date.isocalendar()  # datetime.IsoCalendarDate(year=2024, week=36, weekday=1)
        return f"Week {_iso_date[1]} Year {_iso_date[0]}"


admin.site.register(Week, WeekAdmin)