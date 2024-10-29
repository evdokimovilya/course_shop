# Generated by Django 5.0.3 on 2024-06-11 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_coursecategory_alter_course_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursecategory',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
