from django.urls import path
from .views import CreateSensorAPIView, SensorUpdateView, MeasurementCreateView, SensorListAPIView, SensorRetrieveAPIView

urlpatterns = [
    path('sensors/create/', CreateSensorAPIView.as_view(), name='create-sensor'),
    path('sensors/<int:pk>/update/', SensorUpdateView.as_view(), name='update-sensor'),
    path('measurements/create/', MeasurementCreateView.as_view(), name='create-measurement'),
    path('sensors/list/', SensorListAPIView.as_view(), name='get-list-sensor'),
    path('sensors/<int:id>/', SensorRetrieveAPIView.as_view(), name='get-list-sensor-id'),
]
