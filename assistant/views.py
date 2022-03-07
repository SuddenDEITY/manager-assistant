from unittest import result
from django.shortcuts import render
from django.views import View
from django.utils import timezone
from .models import Client, Equipment, Eq_Category, Eq_Characteristics, Question, Answer
import json
# Create your views here.

class BaseView(View):
    def get(self, request):
        clients = Client.objects.all()
        categories = Eq_Category.objects.all()
        first_question = Question.objects.get(id=1)
        try:
            next_question = Question.objects.get(id=first_question.id+1)
        except:
            next_question = 'Больше вопросов нет'
            
        answers = Answer.objects.filter(question__id=first_question.id)
        return render(request, 'assistant/assistant-template.html', {'clients':clients,'categories': categories,
                                                                     'first_question':first_question,'answers':answers,
                                                                     'next_question':next_question})

class AjaxGetEquipmentView(View):
    def get(self, request, category_id, filter_by):
        filter = json.loads(filter_by)
        equipments = Equipment.objects.filter(category__id=category_id).filter(**filter)
        result_equipments = equipments
        return render(request, 'assistant/ajax_equipment.html', {'equipments': equipments})

class AjaxGetCharacteristicView(View):
    def get(self, request, equipment_id):
        characteristics = Eq_Characteristics.objects.filter(equipment__id=equipment_id)
        return render(request, 'assistant/ajax_characteristic.html', {'characteristics': characteristics})

class AjaxQuestionView(View):
    def get(self, request, question_id):
        #sorted_by
        #json_sorted_by = json.loads(sorted_by)
        try:
            question = Question.objects.get(id=question_id+1)
            answers = Answer.objects.filter(question__id=question.id)
        except:
            question = "Вопросов больше нет"
            answers = None
        try:
            next_question = Question.objects.get(id=question_id+2)
        except:
            next_question = "Вопросов больше нет"
        
        return render(request, 'assistant/ajax_question.html', {'question': question, 'ajax_next_question': next_question, 'answers':answers})

class AjaxEquipmentFilterView(View):
    def get(self, request, answer_id, filter_by):
        filter = json.loads(filter_by)
        print(filter)
        answer = Answer.objects.get(id=answer_id)
        if answer.type=='withdata':
            answer_sort_field = answer.sort_field
            answer_sort_value = answer.sort_value
            equipment = Equipment.objects.filter(**{answer_sort_field : answer_sort_value}).filter(**filter)
            category_list = list(set([eq.category for eq in equipment if eq.category]))
        return render(request, 'assistant/ajax_category_filter.html', {'category_list': category_list, 'filter_by_value': answer_sort_value, 'filter_by_field': answer_sort_field}) 
    
    
