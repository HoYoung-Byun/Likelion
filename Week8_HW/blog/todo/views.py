from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .models import Todo
from .serializers import  *

# Create your views here.


class TodoShowAll(APIView):

    def get(self, request):
        todos = Todo.objects.filter(complete=False)
        serializer = TodoShowAllSerializer(todos, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)


    def post(self, request):
        serializer = TodoCreateFixSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class TodoDetail(APIView):

    def get_object(self, pk):
        return Todo.objects.get(pk=pk)
    
    def get(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def put(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoCreateFixSerializer(todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoCompleteList(generics.ListAPIView):
    queryset = Todo.objects.filter(complete=True)
    serializer_class = TodoSerializer



class TodoMakeComplete(APIView) :

    def get_object(self, pk):
        return Todo.objects.get(pk=pk)
    
    def get(self, request, pk):
        todo = self.get_object(pk)
        todo.complete = True
        todo.save()
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    