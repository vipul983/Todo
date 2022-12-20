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
        # todo_items = TodoItem.objects.all()
        # serializer = TodoListSerializer(todo_items, many=True)
        # json_data = JSONRenderer().render(serializer.data)
        # print(json_data)
        # ans=json.loads(json_data)
        # return JsonResponse(ans, safe=False)
        todo_item = TodoItem.objects.all()
        # serializer = TodoListSerializer(todo_items, many=True)
        # json_data = JSONRenderer().render(serializer.data)
        records_list = list(todo_item.values())
        json_data = json.dumps(records_list)
        # todo_items = json.dumps(todo_items.__dict__)
        print(json_data)
        ans=json.loads(json_data)
        return JsonResponse(ans, safe=False)
        #return JsonResponse({"models_to_return": list(queryset)})
        
        
        
    # def post(self, request):
    #     post_body = json.loads(request.body)
    #     data = {'text': post_body['title'], 'done': False}
    #     print(data)
    #     serializer = TodoListSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data)
    #     return JsonResponse(serializer.errors, status=400)

    def post(self, request):
        post_body = json.loads(request.body)
        data = {'text': post_body['title'], 'done': False}
        print(data)
        # serializer = TodoListSerializer(data=data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return JsonResponse(serializer.data)
        # return JsonResponse(serializer.errors, status=400)

        todoitem = TodoItem()
        todoitem.text = data['text']
        todoitem.done = data['done']
        # json_data = json.dumps(todoitem)
        # print(json_data)
    # Save the instance to the database
        todoitem.save()
        return Response({"status" : "200"})

