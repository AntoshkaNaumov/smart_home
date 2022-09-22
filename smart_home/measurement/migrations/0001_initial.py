# Generated by Django 4.1.1 on 2022-09-22 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(verbose_name='температура при изменении')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='дата измерения')),
                ('sensor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor', verbose_name='ID датчика')),
            ],
        ),
    ]