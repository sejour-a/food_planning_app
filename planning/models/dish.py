from django.db import models
from django.contrib import admin

from planning.admin import DishAdmin


DESC_MAX_DISPLAYED_LENGTH_WITH_ELLIPSIS = 30
DESC_ELLIPSIS_TEXT = '...'

DESC_MAX_DISPLAYED_LENGTH = DESC_MAX_DISPLAYED_LENGTH_WITH_ELLIPSIS - len(DESC_ELLIPSIS_TEXT)


class Dish(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=1024, blank=True)
    recipe = models.TextField(max_length=4096, blank=True)
    photo = models.ImageField(blank=True)
    recipe_url = models.URLField(null=True, blank=True)
    ingredients = models.ManyToManyField("groceries.item", blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        description_blurb = ''

        if self.description:
            if len(self.description) > DESC_MAX_DISPLAYED_LENGTH_WITH_ELLIPSIS:
                description_blurb = f" ({self.description[0:DESC_MAX_DISPLAYED_LENGTH]}{DESC_ELLIPSIS_TEXT})"
            else:
                description_blurb = f" ({self.description})"

        return f"""dish item: "{self.name}"{description_blurb} - Ingredients: {[i.name for i in self.ingredients.all()]}"""

    class Meta:
        verbose_name_plural = "dishes"


admin.site.register(Dish, DishAdmin)