# Generated by Django 5.0.3 on 2024-06-12 06:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_coursecategory_options_alter_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_lectures', to='course.course'),
        ),
    ]
