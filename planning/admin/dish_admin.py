from django.contrib import admin


class DishAdmin(admin.ModelAdmin):
    filter_horizontal = ('ingredients',)
