from django.shortcuts import render
from .models import questionsModel, questionAnswerModel, GradedModel
from .serializers import questionSerializer, questionAnswerSerializer, gradesSerializer
import io
from rest_framework.parsers import JSONParser 
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def insertQuestions(request):
    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        serializer = questionSerializer(data = pythonData)
        
        if serializer.is_valid():
            serializer.save()    
            res = {'msg': 'Data Created '}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        jsonData = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = "application/json")    



def getQuestions(request):
    questions = questionsModel.objects.all()
    serializer = questionSerializer(questions, many = True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = "application/json")

@csrf_exempt
def insertAnswers(request):
    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        serializer = questionAnswerSerializer(data = pythonData)
        
        if serializer.is_valid():
            serializer.save()    
            res = {'msg': 'Data Created '}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        jsonData = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = "application/json")    

@csrf_exempt
def insertGrades(request):
    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        serializer = gradesSerializer(data = pythonData)
        
    if serializer.is_valid():
        serializer.save()    
        res = {'msg': 'Data Created '}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type = 'application/json')
    
    jsonData = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type = "application/json")    
    

def getGrades(request):
    questions = GradedModel.objects.all()
    serializer = gradesSerializer(questions, many = True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = "application/json")
