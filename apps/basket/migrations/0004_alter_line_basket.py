# Generated by Django 5.0.3 on 2024-06-18 19:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0003_alter_line_basket_alter_line_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket_lines', to='basket.basket'),
        ),
    ]
