from rest_framework import serializers

from projects import models


class MainInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MainInformation
        fields = [
            'language',
            'title',
            'text',
        ]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = [
            'image',
            'description',
            'text',
        ]


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Technology
        fields = [
            'image',
            'title'
        ]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = [
            "order",
            "language",
            "title",
            "link",
            "image",
            "description",
            "created",
            "technologies",
        ]


class LearnProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LearnProject
        fields = [
            "order",
            "language",
            "title",
            "link",
            "image",
            "description",
            "created",
            "technologies",
        ]
