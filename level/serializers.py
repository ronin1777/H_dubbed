from rest_framework import serializers

from level.models import Level


class LevelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'
