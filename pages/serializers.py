from rest_framework import serializers
from .models import Snack


class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snack
        fields = ['id', 'name', 'description', 'reviewer', 'rating', 'image_url', 'created_at', 'updated_at']