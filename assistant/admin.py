from django.contrib import admin

from django.contrib import admin
from .models import Question, Answer, Client
# Register your models here.

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    class Media:
        js = (
              '/static/admin/js/hide_question.js',
              )
    inlines = [
        AnswerInline,
    ]

class AnswerAdmin(admin.ModelAdmin):
    class Media:
        js = (
              '/static/admin/js/hide_answer.js',
              )

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Client)