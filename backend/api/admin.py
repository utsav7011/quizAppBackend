from django.contrib import admin
from .models import questionsModel, questionAnswerModel, GradedModel

# Register your models here.
@admin.register(questionsModel)
class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'subject']
    
@admin.register(questionAnswerModel)
class QuestionAnswerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'subject', 'answer']

@admin.register(GradedModel)
class GradedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'subject', 'answer', 'grade']
