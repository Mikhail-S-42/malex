# Generated by Django 3.2.9 on 2021-12-28 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0003_alter_access_access'),
    ]

    operations = [
        migrations.RenameField(
            model_name='access',
            old_name='start_url',
            new_name='startUrl',
        ),
    ]
