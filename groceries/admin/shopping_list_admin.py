from django.contrib import admin


class ShoppingListAdmin(admin.ModelAdmin):
    filter_horizontal = ('items',)
