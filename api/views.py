from django.shortcuts import render

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import *
from django.db.models import Q
from django.core.paginator import Paginator


class UserList(generics.ListCreateAPIView):
    serializer_class = UsersSerializer

    def get_queryset(self):
        name = self.request.GET.get('name')
        limit = self.request.GET.get('limit')
        if limit is not None:
            limit = int(limit)
        sort_by_param = self.request.GET.get('sort')
        page = self.request.GET.get('page')
        if name is None and limit is None and sort_by_param is None and page is None:
            return Users.objects.all()
        else:
            if name is None:
                name = ""
            if sort_by_param is None:
                sort_by_param = "id"
            if page is None:
                page = 1
            queryset = Users.objects.filter(
                Q(first_name__contains=name) | Q(last_name__contains=name)).order_by(str(sort_by_param))[:limit]
            paginator = Paginator(queryset, 5)
            users = paginator.page(page)
            return users

    def perform_create(self, serializer):
        return serializer.save()


class UserDetail(APIView):
    def get_query(self, id):
        try:
            queryset = Users.objects.get(id=id)
            return queryset
        except Users.DoesNotExist:
            return

    def get(self, request, id):
        if not self.get_query(id):
            Response('User Not Found', status=status.HTTP_404_NOT_FOUND)
        serializer = UsersSerializer(self.get_query(id))
        return Response(serializer.data)

    def put(self, request, id):
        serializer = UsersSerializer(
            self.get_query(id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        queryset = self.get_query(id)
        queryset.delete()
        return Response(status=status.HTTP_200_OK)
