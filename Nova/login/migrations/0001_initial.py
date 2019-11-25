# Generated by Django 2.2.5 on 2019-11-25 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('class_id', models.CharField(max_length=50, null=True)),
                ('class_name', models.CharField(max_length=50, null=True)),
                ('class_number', models.IntegerField(null=True)),
                ('class_teacher', models.CharField(max_length=50, null=True)),
                ('class_credits', models.IntegerField(null=True)),
                ('class_desc', models.CharField(max_length=50, null=True)),
                ('class_day', models.CharField(max_length=50, null=True)),
                ('class_times', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50, null=True)),
                ('class_id', models.CharField(max_length=50, null=True)),
                ('title', models.CharField(max_length=50, null=True)),
                ('desc', models.CharField(max_length=50, null=True)),
                ('due_date', models.CharField(max_length=50, null=True)),
                ('due_time', models.CharField(max_length=50, null=True)),
                ('total_submissions', models.IntegerField(null=True)),
                ('missing_submissions', models.IntegerField(null=True)),
                ('missing_submissions_names', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('student_id', models.CharField(max_length=50, null=True)),
                ('grade_letter', models.CharField(max_length=50, null=True)),
                ('grade_number', models.CharField(max_length=50, null=True)),
                ('class_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Classes')),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reminder_title', models.CharField(max_length=50, null=True)),
                ('reminder_message', models.CharField(max_length=200, null=True)),
                ('reminder_id', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('nova_id', models.IntegerField(null=True)),
                ('school', models.CharField(max_length=50, null=True)),
                ('department', models.CharField(max_length=50, null=True)),
                ('teacher_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('nova_id', models.CharField(max_length=50, null=True)),
                ('school', models.CharField(max_length=50, null=True)),
                ('student_id', models.CharField(max_length=50, null=True)),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
                ('credits_taken', models.IntegerField(null=True)),
                ('credits_current', models.IntegerField(null=True)),
                ('major', models.CharField(max_length=50, null=True)),
                ('classes', models.ManyToManyField(to='login.Classes')),
                ('grades', models.ManyToManyField(to='login.Grade')),
            ],
        ),
        migrations.AddField(
            model_name='classes',
            name='contents',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Content'),
        ),
    ]
