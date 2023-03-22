from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer
from measurement.models import Sensor, Measurement
from django.shortcuts import get_object_or_404
from django.utils import timezone


class CreateSensorAPIView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def perform_create(self, serializer):
        serializer.save(created_at=timezone.now())


class SensorUpdateView(UpdateAPIView):
    serializer_class = SensorDetailSerializer
    queryset = Sensor.objects.all()
    lookup_url_kwarg = ('name', 'description')

    def perform_update(self, serializer):
        serializer.save(updated_at=timezone.now())


class MeasurementCreateView(CreateAPIView):
    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()

    def perform_create(self, serializer):
        sensor_id = self.request.data.get('sensor_id')
        sensor = get_object_or_404(Sensor, id=sensor_id)
        serializer.save(sensor=sensor, created_at=timezone.now())


class SensorListAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SensorRetrieveAPIView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    lookup_field = 'id'
