from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Usuario(AbstractBaseUser):
    USERNAME_FIELD = 'email'

    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('Email', unique=True, max_length=100, db_index=True)
    is_staff = models.BooleanField('Permitir acesso como gerenciador do sistema', default=False)
    is_active = models.BooleanField('Ativo', default=True, help_text='Liberar acesso ao sistema')

    objects = UserManager()

    class Meta:
        ordering = ['nome']
        verbose_name = _('usuário')
        verbose_name_plural = _('usuários')

    def __str__(self):
        return self.nome
