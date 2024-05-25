import json
from car.serializers import CarSerializer
from car.models import Car


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return json.dumps(serializer.data).encode("utf-8")


def deserialize_car_object(json_data: bytes) -> Car:
    data = json.loads(json_data.decode("utf-8"))
    serializer = CarSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        return serializer.save()
    return
