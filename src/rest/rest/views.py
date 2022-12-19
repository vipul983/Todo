from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json, logging, os
# from pymongo import MongoClient

from django.http import JsonResponse
from .models import TodoItem
from .serializers import TodoItemSerializer
# mongo_uri = 'mongodb+srv://vipul1234:vipul1234@cluster0.agkcmfj.mongodb.net/test'
# db = MongoClient(mongo_uri)['test_db']

#client = pymongo.MongoClient('mongodb+srv://username:password@HOSTNAME/DATABASE_NAME?authSource=admin&tls=true&tlsCAFile=<PATH_TO_CA_FILE>')

class TodoListView(APIView):

    def get(self, request):
        # Implement this method - return all todo items from db instance above.
        todo_items = TodoItem.objects.all()
        serializer = TodoItemSerializer(todo_items, many=True)
        return JsonResponse(serializer.data, safe=False)
       # return Response({}, status=status.HTTP_200_OK)
        
    def post(self, request):
        # Implement this method - accept a todo item in a mongo collection, persist it using db instance above.
        post_body = json.loads(request.body)
        data = {'text': post_body['title'], 'done': False}
        print(data)
        serializer = TodoItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

        #return Response({}, status=status.HTTP_200_OK)

