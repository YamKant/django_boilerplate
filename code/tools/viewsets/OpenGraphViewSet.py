from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.shortcuts import render, redirect

class OpenGraphViewSet(ModelViewSet):
    @action(detail=False, methods=['post'])
    def getOpenGraph(self, req):
        try:
            return Response(True, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

open_graph_list = OpenGraphViewSet.as_view({
    'post': 'getOpenGraph',
})