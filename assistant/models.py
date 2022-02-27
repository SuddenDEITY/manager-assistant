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
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)

    def __str__(self) -> str:
        return f"{self.answer_title} | {self.question.question_title}"

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'



