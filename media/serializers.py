from rest_framework import serializers

from media.models import MediaModel


class MediaSerializers(serializers.ModelSerializer):
    class Meta:
        model = MediaModel
        fields = '__all__'
