# Generated by Django 5.0.3 on 2024-03-31 22:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0011_rename_place_comment_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
