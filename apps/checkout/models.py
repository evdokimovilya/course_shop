from django.db import models

from apps.user_profile.models import User
from apps.user_profile.models import CourseProfile
from apps.basket.models import Basket


class Order(models.Model):
    class StatusChoices(models.TextChoices):
        WAITING = 'Waiting', 'В обработке'
        CLOSED = 'Closed', 'Обработан'

    user = models.ForeignKey(User, related_name='user_orders', on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    status = models.CharField(choices=StatusChoices, default=StatusChoices.WAITING, max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user} {self.created_date}'
    

    def set_complete(self):
        self.status = self.StatusChoices.CLOSED
        self.save()

        for line in self.basket.basket_lines.all():
            CourseProfile.objects.create(profile=self.user.profile, course=line.course)


