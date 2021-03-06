# Generated by Django 3.2.9 on 2021-12-28 03:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dateFix', models.DateField(blank=True, help_text='Дата фиксаций', null=True)),
                ('dateGet', models.DateTimeField(help_text='Дата получения')),
                ('dateSend', models.DateTimeField(blank=True, help_text='Дата отправки', null=True)),
                ('amount', models.IntegerField(help_text='Количество нарушений')),
                ('device', models.ForeignKey(help_text='Прибор', on_delete=django.db.models.deletion.PROTECT, to='devices.device')),
                ('operator', models.ForeignKey(help_text='Оператор', on_delete=django.db.models.deletion.PROTECT, to='account.profile')),
            ],
            options={
                'ordering': ['dateFix', 'device'],
            },
        ),
        migrations.CreateModel(
            name='ErrorType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название', max_length=255)),
                ('desc', models.CharField(help_text='Описание', max_length=1023)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archive', models.ForeignKey(help_text='Архив', on_delete=django.db.models.deletion.PROTECT, to='violations.archive')),
                ('error', models.ForeignKey(help_text='Ошибка', on_delete=django.db.models.deletion.PROTECT, to='violations.errortype')),
            ],
            options={
                'ordering': ['archive'],
            },
        ),
    ]
