from rest_framework import serializers

from planning.models import Week
from planning.serializers import WeekSerializer

from groceries.models import ShoppingList


class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = '__all__'