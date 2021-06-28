from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.base_model import BaseModel


class Cliente(BaseModel):
    nome = models.CharField(_('Nome'), max_length=100)
    idade = models.CharField(_('Idade'), max_length=3)
    cidade = models.CharField('Cidade', max_length=70, blank=True, null=True)

    objects = UserManager()

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
