# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    vatin = models.PositiveIntegerField(verbose_name='ИНН', blank=True, null=True)
    account = models.DecimalField(verbose_name='счет', max_digits=10, decimal_places=2, blank=True, null=True)