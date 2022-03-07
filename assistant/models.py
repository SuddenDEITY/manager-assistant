from operator import mod
from statistics import mode
from tkinter import N
from unicodedata import category
from django.db import models

# Create your models here.

class Client(models.Model):
    full_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Question(models.Model):
    question_title = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.question_title
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

TYPE_CHOICES = (
    ("withdata", "Логический"),
    ("withoutdata", "Справочный"),

)

class Answer(models.Model):
    answer_title = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='withoutdata')
    sort_field = models.CharField(max_length=50, blank=True, default=None)
    sort_value = models.CharField(max_length=50, blank=True, default=None)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None, related_name='answers')

    def __str__(self) -> str:
        return f"{self.answer_title} | {self.question.question_title}"

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

class Eq_Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Eq_Drilling(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Тип бура'
        verbose_name_plural = 'Типы бура'


class Equipment(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Eq_Category, on_delete=models.CASCADE, default=None, related_name='cat_equipment')
    drilling_type = models.ForeignKey(Eq_Drilling, on_delete=models.CASCADE, default=None, related_name='equipment')


    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудования'


class Eq_Characteristics(models.Model):
    name = models.CharField(max_length=300)
    value = models.CharField(max_length=100, default=0)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, default=None, related_name='characteristics')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'


