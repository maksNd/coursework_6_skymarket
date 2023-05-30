from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles:
    # TODO закончите enum-класс для пользователя
    USER = 'user'
    ADMIN = 'admin'

    choices = (
        (USER, 'Пользователь'),
        (ADMIN, 'Админ')
    )


class User(AbstractBaseUser):
    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту

    email = models.EmailField(max_length=100, validators=[MinLengthValidator(1)], unique=True)
    first_name = models.CharField(max_length=100, validators=[MinLengthValidator(1)], verbose_name="Имя")
    last_name = models.CharField(max_length=100, validators=[MinLengthValidator(1)], verbose_name="Фамилия")
    phone = PhoneNumberField(max_length=100, validators=[MinLengthValidator(1)], verbose_name="Номер телефона")
    role = models.CharField(max_length=6, choices=UserRoles.choices, default="user", verbose_name="Роль")
    image = models.ImageField(verbose_name="Картинка", null=True, blank=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'password']

    objects = UserManager()



    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def __str__(self):
        return self.email
