from rest_framework import serializers
from .models import questionAnswerModel, questionsModel, GradedModel

class questionSerializer(serializers.Serializer):
    question = serializers.CharField()
    subject = serializers.CharField(max_length = 200)
    
    def create(self, validate_data):
        return questionsModel.objects.create(**validate_data)

class questionAnswerSerializer(serializers.Serializer):
    question = serializers.CharField()
    subject = serializers.CharField(max_length= 200)
    answer = serializers.CharField()
    
    def create(self, validate_data):
        return questionAnswerModel.objects.create(**validate_data)
    
class gradesSerializer(serializers.Serializer):
    question = serializers.CharField()
    subject = serializers.CharField(max_length= 200)
    answer = serializers.CharField()
    grade = serializers.CharField(max_length = 50)
    
    def create(self, validate_data):
        return GradedModel.objects.create(**validate_data)