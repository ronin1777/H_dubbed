from rest_framework import serializers

from media.models import MediaModel, BucketObjects


class MediaSerializers(serializers.ModelSerializer):
    class Meta:
        model = MediaModel
        fields = '__all__'


class BucketObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = BucketObjects
        fields = '__all__'
