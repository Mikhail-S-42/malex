# Generated by Django 3.2.9 on 2021-12-28 03:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('pos', models.CharField(help_text='Должность', max_length=255)),
                ('sur', models.CharField(help_text='Фамилия', max_length=255)),
                ('name', models.CharField(help_text='Имя', max_length=255)),
                ('mid', models.CharField(help_text='Отчество', max_length=255)),
                ('city', models.CharField(help_text='Город', max_length=255, null=True)),
                ('addr', models.CharField(help_text='Адрес', max_length=255, null=True)),
                ('tel', models.CharField(help_text='Контактный телефон', max_length=16)),
                ('dateEmploy', models.DateField(help_text='Дата приёма на работу')),
                ('dateDis', models.DateField(blank=True, help_text='Дата увольнения', null=True)),
                ('group', models.ForeignKey(help_text='Группа', on_delete=django.db.models.deletion.PROTECT, to='auth.group')),
                ('user', models.ForeignKey(help_text='Пользователь', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['sur', 'name', 'mid'],
            },
        ),
    ]
