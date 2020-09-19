from rest_framework import viewsets

from projects import models, serializers


class MainInformationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.MainInformation.objects.all()
    serializer_class = serializers.MainInformationSerializer


class ContactViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


class TechnologyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Technology.objects.all()
    serializer_class = serializers.TechnologySerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class LearnProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.LearnProject.objects.all()
    serializer_class = serializers.LearnProjectSerializer
