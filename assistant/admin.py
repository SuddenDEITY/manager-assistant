from django.contrib import admin

from django.contrib import admin
from .models import Question, Answer, Client, Equipment, Eq_Drilling, Eq_Category, Eq_Characteristics
# Register your models here.

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]

class CharacteristicInline(admin.TabularInline):
    model = Eq_Characteristics
    extra = 0

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'drilling_type']
    list_select_related = (
        'drilling_type',
    )
    inlines = [
        CharacteristicInline,
    ]

class AnswerAdmin(admin.ModelAdmin):
    class Media:
        js = (
              '/static/admin/js/hide_answer.js',
              )

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Client)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Eq_Drilling)
admin.site.register(Eq_Category)
admin.site.register(Eq_Characteristics)