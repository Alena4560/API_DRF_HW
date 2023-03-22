from rest_framework import serializers
from measurement.models import Sensor, Measurement
from datetime import datetime, timedelta


class MeasurementSerializer(serializers.ModelSerializer):
    sensor_id = serializers.IntegerField()
    temperature = serializers.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        model = Measurement
        fields = ['id', 'sensor_id', 'temperature', 'created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


now = datetime.now()
then = now - timedelta(minutes=5)


sensor1 = Sensor.objects.create(name='ESP32', description='Датчик на кухне за холодильником')
measurement1 = Measurement.objects.create(sensor=sensor1, temperature=25.5, created_at=now)
measurement2 = Measurement.objects.create(sensor=sensor1, temperature=26.5, created_at=then)

sensor2 = Sensor.objects.create(name='ESP32', description='Перенес датчик на балкон')
measurement3 = Measurement.objects.create(sensor=sensor2, temperature=20.0, created_at=now)
measurement4 = Measurement.objects.create(sensor=sensor2, temperature=21.0, created_at=then)

sensor1_serializer = SensorDetailSerializer(sensor1)
sensor2_serializer = SensorDetailSerializer(sensor2)


print(sensor1_serializer.data)
print(sensor2_serializer.data)
