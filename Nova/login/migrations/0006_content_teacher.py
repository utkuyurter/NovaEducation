# Generated by Django 2.2.5 on 2019-11-25 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_content_affect'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='teacher',
            field=models.IntegerField(null=True),
        ),
    ]
