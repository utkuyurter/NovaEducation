# Generated by Django 2.2.5 on 2019-11-25 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gpa_projected',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
    ]
