from django.db import models


class MainInformation(models.Model):
    LANGUAGES = [
        ('pl', 'pl'),
        ('en', 'en'),
    ]
    language = models.CharField(max_length=2, choices=LANGUAGES)
    title = models.CharField(max_length=30)
    text = models.TextField()


class Contact(models.Model):
    image = models.ImageField()
    description = models.CharField(max_length=20)
    text = models.CharField(max_length=50)
    link = models.BooleanField(default=False)


class Technology(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=20)


class Project(models.Model):
    LANGUAGES = [
        ('pl', 'pl'),
        ('en', 'en'),
    ]

    order = models.IntegerField()
    language = models.CharField(max_length=2, choices=LANGUAGES)
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
    created = models.DateField()
    technologies = models.ManyToManyField(Technology)

    class Meta:
        get_latest_by = 'order'
        ordering = ['order']


class LearnProject(models.Model):
    LANGUAGES = [
        ('pl', 'pl'),
        ('en', 'en'),
    ]

    order = models.IntegerField()
    language = models.CharField(max_length=2, choices=LANGUAGES)
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
    created = models.DateField()
    technologies = models.ManyToManyField(Technology)

    class Meta:
        get_latest_by = 'order'
        ordering = ['order']
