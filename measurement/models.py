from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    sensor = models.ForeignKey('Sensor', related_name='measurements', on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return f'Temperature: {self.temperature}, Created at: {self.created_at}'
