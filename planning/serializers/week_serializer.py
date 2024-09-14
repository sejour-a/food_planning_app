from rest_framework import serializers

from planning.models import Week


class WeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Week
        fields = '__all__'