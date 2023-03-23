from rest_framework import serializers
from measurement.models import Sensor, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    sensor_id = serializers.IntegerField()
    temperature = serializers.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        model = Measurement
        fields = ['sensor_id', 'temperature', 'created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
