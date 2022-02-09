from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from .models import *
from .serializers import ProblemaSerializer, ReplySerializer, CommentSerializer


class ProblemViewSet(ModelViewSet):
    queryset = Problema.objects.all()
    serializer_class = ProblemaSerializer

    def get_serializer_context(self):
        return {'action': self.action}

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q')
        queryset = self.get_queryset().filter(Q(title__icontains=query) | Q(description__icontains=query))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)


class ReplyViewSet(ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

    def get_serializer_context(self):
        return {'action': self.action}


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


