# Generated by Django 3.2.9 on 2021-12-28 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='access',
            name='access',
            field=models.BooleanField(default=False, help_text='Настройка доступа'),
        ),
    ]
