from django.urls import path
from .views import BaseView, AjaxGetEquipmentView, AjaxGetCharacteristicView, AjaxQuestionView, AjaxEquipmentFilterView
urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('get_equipment/<int:category_id>/<str:filter_by>/', AjaxGetEquipmentView.as_view(), name='get_equipment'),
    path('get_characteristic/<int:equipment_id>/', AjaxGetCharacteristicView.as_view(), name='get_characteristic'),
    path('apply_answer/<int:question_id>/', AjaxQuestionView.as_view(), name='apply_answer'),
    path('get_filter_val/<int:answer_id>/<str:filter_by>/', AjaxEquipmentFilterView.as_view(), name='get_filter_val'),

]
