from django.db import models

from utils.gerador_hash import gerar_hash


class BaseModel(models.Model):
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    is_active = models.BooleanField('Cadastro ativo', default=True)
    dt_cadastro = models.DateTimeField('Dt. cadastro', auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-dt_cadastro']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_hash()

        super().save(*args, **kwargs)
