from django.urls import path, include

from rest_framework.routers import DefaultRouter

from projects import views

app_name = 'projects'

router = DefaultRouter()
router.register(r'main-information', viewset=views.MainInformationViewSet)
router.register(r'contact', viewset=views.ContactViewSet)
router.register(r'techonology', viewset=views.TechnologyViewSet)
router.register(r'project', viewset=views.ProjectViewSet)
router.register(r'learn-project', viewset=views.LearnProjectViewSet)

urlpatterns = [
    path('', include(router.urls))
]
