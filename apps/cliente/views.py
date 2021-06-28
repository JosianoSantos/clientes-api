from django.shortcuts import get_object_or_404
from rest_framework import generics

from apps.cliente.models import Cliente
from apps.cliente.serializers import ClienteSerializer, ClienteListSerializer


class ClienteList(generics.ListAPIView):
    serializer_class = ClienteListSerializer
    queryset = Cliente.objects.all()

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        idade = self.request.query_params.get('idade', None)
        cidade = self.request.query_params.get('cidade', None)
        ordenar = self.request.query_params.get('ordenar', None)

        if id:
            self.queryset = self.queryset.filter(id=id)

        if nome:
            self.queryset = self.queryset.filter(nome__icontains=nome)

        if idade:
            self.queryset = self.queryset.filter(idade=idade)

        if cidade:
            self.queryset = self.queryset.filter(cidade__icontains=cidade)

        if ordenar:
            self.queryset = self.queryset.order_by(ordenar)

        return self.queryset.all()


class ClienteCreate(generics.CreateAPIView):
    serializer_class = ClienteSerializer


class ClienteDetail(generics.RetrieveAPIView):
    serializer_class = ClienteListSerializer
    queryset = Cliente.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.kwargs['id'])
        return obj


class ClienteDelete(generics.DestroyAPIView):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.kwargs['id'])
        return obj


class ClienteUpdate(generics.UpdateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.kwargs['id'])
        return obj
