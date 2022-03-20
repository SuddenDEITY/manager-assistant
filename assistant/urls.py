from django.urls import path
from .views import BaseView, AjaxGetEquipmentView, AjaxGetCharacteristicView, AjaxGetAllDataView
urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('get_equipment/<int:category_id>/<str:filter_by>/', AjaxGetEquipmentView.as_view(), name='get_equipment'),
    path('get_all_data/<int:answer_id>/<int:question_id>/<str:filter_by>/', AjaxGetAllDataView.as_view(), name='get_all_data'),
    path('get_characteristic/<int:equipment_id>/', AjaxGetCharacteristicView.as_view(), name='get_characteristic')

]
