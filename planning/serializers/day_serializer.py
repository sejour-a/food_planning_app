from rest_framework import serializers

from planning.models import Day


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'