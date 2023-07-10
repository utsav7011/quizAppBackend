from django.db import models

# Create your models here.

class questionsModel(models.Model):
    question = models.TextField()
    subject = models.CharField(max_length= 200)
    
class questionAnswerModel(models.Model):
    question = models.TextField()
    subject = models.CharField(max_length= 200)
    answer = models.TextField()
    
class GradedModel(models.Model):
    question = models.TextField()
    subject = models.CharField(max_length= 200)
    answer = models.TextField()
    grade = models.CharField(max_length= 50)
    
