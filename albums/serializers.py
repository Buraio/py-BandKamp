from rest_framework import serializers

from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["id", "name", "year", "user_id"]

    def create(self, validated_data):
        return Album.objects.create(**validated_data)
