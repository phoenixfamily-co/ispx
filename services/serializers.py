from rest_framework import serializers
from .models import Services
from category.models import Category


class ServicesSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())

    class Meta:
        model = Services
        fields = '__all__'

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        service = Services.objects.create(**validated_data)
        service.categories.set(categories_data)
        return service

    def update(self, instance, validated_data):
        categories_data = validated_data.pop('categories')
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        instance.categories.set(categories_data)
        return instance
