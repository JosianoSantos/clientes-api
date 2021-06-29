import json

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from .models import Cliente
from .serializers import ClienteListSerializer

client = Client()


class GetTodosClientesTest(TestCase):

    def setUp(self):
        Cliente.objects.create(
            nome='José da Silva', idade=20, cidade='Santa Maria')
        Cliente.objects.create(
            nome='Maria da Silva', idade=30, cidade='Florianópolis')

    def test_get_todos_clientes(self):
        # get API response
        response = client.get(reverse('cliente:list'))
        # get data from db
        clientes = Cliente.objects.all()
        serializer = ClienteListSerializer(clientes, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetClienteTest(TestCase):

    def setUp(self):
        self.jose = Cliente.objects.create(
            nome='José da Silva', idade=20, cidade='Santa Maria')
        self.maria = Cliente.objects.create(
            nome='Maria da Silva', idade=30, cidade='Florianópolis')

    def test_get_cliente_valido(self):
        response = client.get(
            reverse('cliente:detail', kwargs={'id': self.jose.pk}))
        cliente = Cliente.objects.get(pk=self.jose.pk)
        serializer = ClienteListSerializer(cliente)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_cliente_invalido(self):
        response = client.get(
            reverse('cliente:detail', kwargs={'id': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateClienteTest(TestCase):

    def setUp(self):
        self.valid_payload = {
            'nome': 'José da Silva',
            'idade': 20,
            'cidade': 'Santa Maria',
        }
        self.invalid_payload = {
            'nome': None,
            'idade': 10,
            'cidade': 'Santa Maria',
        }

    def test_create_cliente_valido(self):
        response = client.post(
            reverse('cliente:create'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_cliente_invalido(self):
        response = client.post(
            reverse('cliente:create'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateClienteTest(TestCase):

    def setUp(self):
        self.jose = Cliente.objects.create(
            nome='José da Silva', idade=20, cidade='Santa Maria')
        self.maria = Cliente.objects.create(
            nome='Maria da Silva', idade=30, cidade='Florianópolis')
        self.valid_payload = {
            'nome': 'José da Silva',
            'idade': 20,
            'cidade': 'Santa Maria',
        }
        self.invalid_payload = {
            'nome': '',
            'idade': 10,
            'cidade': 'Santa Maria',
        }

    def test_update_cliente_valido(self):
        response = client.put(
            reverse('cliente:update', kwargs={'id': self.jose.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_cliente_invalido(self):
        response = client.put(
            reverse('cliente:update', kwargs={'id': self.jose.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteClienteTest(TestCase):

    def setUp(self):
        self.jose = Cliente.objects.create(
            nome='José da Silva', idade=20, cidade='Santa Maria')
        self.maria = Cliente.objects.create(
            nome='Maria da Silva', idade=30, cidade='Florianópolis')

    def test_cliente_delete_valido(self):
        response = client.delete(
            reverse('cliente:delete', kwargs={'id': self.jose.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_cliente_delete_invalido(self):
        response = client.delete(
            reverse('cliente:delete', kwargs={'id': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
