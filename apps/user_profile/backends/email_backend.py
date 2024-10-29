

from typing import Any
from django.contrib.auth.backends import ModelBackend, BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth import get_user_model
from django.http import HttpRequest


UserModel = get_user_model()


class EmailBackend(ModelBackend):

    def authenticate(self, request, username, password, **kwargs):
        if username is None or password is None:
            return
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
    
    def get_user(self, user_id: int) -> AbstractBaseUser | None:
        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
        return user