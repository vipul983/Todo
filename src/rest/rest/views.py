from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
import json, logging, os
# from pymongo import MongoClient

from django.http import JsonResponse
from .models import TodoItem
from .serializers import TodoListSerializer
# mongo_uri = 'mongodb+srv://vipul1234:vipul1234@cluster0.agkcmfj.mongodb.net/test'
# db = MongoClient(mongo_uri)['test_db']

#client = pymongo.MongoClient('mongodb+srv://username:password@HOSTNAME/DATABASE_NAME?authSource=admin&tls=true&tlsCAFile=<PATH_TO_CA_FILE>')

class TodoListView(APIView):

    def get(self, request):
        todo_items = TodoItem.objects.all()
        serializer = TodoListSerializer(todo_items, many=True)
        json_data = JSONRenderer().render(serializer.data)
        print(json_data)
        ans=json.loads(json_data)
        return JsonResponse(ans, safe=False)
        
        
        
    def post(self, request):
        post_body = json.loads(request.body)
        data = {'text': post_body['title'], 'done': False}
        print(data)
        serializer = TodoListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

