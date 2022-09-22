from django.db import models


# Требуется задать 2 модели (они уже описаны в models.py):
# датчик:
# название
# описание (необязательное, например,
# "спальня" или "корридор на 2 этаже")

class Sensor(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')

# измерение температуры:
# ID датчика
# температура при измерении
# дата измерения


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, verbose_name='ID датчика')
    temperature = models.FloatField(verbose_name='температура при изменении')
    created_at = models.DateTimeField(auto_now=True, verbose_name='дата измерения')
