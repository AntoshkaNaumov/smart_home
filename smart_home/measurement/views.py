# опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics


from .serializers import MeasurementSerializer, SensorDetailSerializer

from .models import Sensor, Measurement


class SensorApiList(generics.ListCreateAPIView):
    # 4. Получить список датчиков.
    # Выдается список с краткой информацией по датчикам: ID, название и описание.
    # 1. Создать датчик. Указываются название и описание датчика.
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreate(generics.ListCreateAPIView):
    # 3. Добавить измерение. Указываются ID датчика и температура.
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorView(generics.RetrieveUpdateAPIView):
    # 5. Получить информацию по конкретному датчику.
    # Выдается полная информация по датчику: ID, название, описание и список всех измерений с температурой и временем.
    # 2. Изменить датчик. Указываются название и/или описание.
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
