
from apps.basket.models import Basket, Line
from apps.course.models import Course

from rest_framework import serializers


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['title', 'image']


class BasketLinesSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Line
        fields = '__all__'