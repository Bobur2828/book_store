# Generated by Django 5.0.3 on 2024-03-31 07:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_rename_descrtiption_books_describtion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='my_app.author', verbose_name='Muallifni tanlang'),
        ),
    ]
