# Generated by Django 3.1.1 on 2020-09-20 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='link',
            field=models.BooleanField(default=False),
        ),
    ]