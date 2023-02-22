from rest_framework import serializers
from task.models import Item


class ItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
