from django.test import TestCase

from .models import Usuario


class UsuarioModelTests(TestCase):
    def setUp(self):
        usuario1 = Usuario.objects.create(nome='Usuario1', email='Usuario1@gmail.com', is_active=True)
        usuario1.set_password('12345678')
        usuario1.save()

        usuario2 = Usuario.objects.create(nome='Usuario2', email='Usuario2@gmail.com', is_active=True)
        usuario2.set_password('12345678')
        usuario2.save()

        usuario3 = Usuario.objects.create(tipo='COMUM', nome='Usuario3', email='Usuario3@gmail.com', is_active=True)
        usuario3.set_password('12345678')
        usuario3.save()

        usuario4 = Usuario.objects.create(tipo='COMUM', nome='Usuario4', email='Usuario4@gmail.com', is_active=True)
        usuario4.set_password('12345678')
        usuario4.save()

        usuario5 = Usuario.objects.create(tipo='ADMINISTRADOR', nome='Usuario5', email='Usuario5@gmail.com', is_active=True)
        usuario5.set_password('12345678')
        usuario5.save()

        usuario6 = Usuario.objects.create(tipo='ADMINISTRADOR', nome='Usuario6', email='Usuario6@gmail.com', is_active=True)
        usuario6.set_password('12345678')
        usuario6.save()

    def test_count_usuario_comun(self):
        self.assertEqual(Usuario.objects.filter(tipo='COMUM').count(), 4)

    def test_count_usuario_administrador(self):
        self.assertEqual(Usuario.objects.filter(tipo='ADMINISTRADOR').count(), 2)
