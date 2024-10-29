from django.db import models

from apps.user_profile.models import User
from apps.course.models import Course


class Basket(models.Model):
    class StatusChoices(models.TextChoices):
        OPEN = 'Open', 'Активная'
        SUBMITTED = 'Submitted', 'Был оформлен заказ'

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='user_baskets')
    status = models.CharField(choices=StatusChoices,
                              max_length=15, default=StatusChoices.OPEN)
    date_created = models.DateTimeField(auto_now_add=True)
    date_submitted = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self) -> str:
        return f'{self.owner} - {self.date_created}'

    def get_total_price(self):
        sum = 0
        for line in self.basket_lines.all():
            sum += line.price
        return sum
    
    def get_course_ids(self):
        return [line.course.id for line in self.basket_lines.all()]


class Line(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='course_lines')
    basket = models.ForeignKey(
        Basket, on_delete=models.CASCADE, related_name='basket_lines')
    price = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Позиция корзины"
        verbose_name_plural = "Позиции корзин"

    def __str__(self) -> str:
        return f'{self.basket} - {self.course}'
