from django.contrib import admin

from projects import models


@admin.register(models.MainInformation)
class MainInformationAdmin(admin.ModelAdmin):
    list_display = [
        'language',
        'title',
    ]


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'description',
    ]


@admin.register(models.Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'language',
        'order',
        'title',
        'created'
    ]


@admin.register(models.LearnProject)
class LearnProjectAdmin(admin.ModelAdmin):
    list_display = [
        'language',
        'order',
        'title',
        'created',
    ]
