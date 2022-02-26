from django.shortcuts import render
from django.views import View
from django.utils import timezone
# Create your views here.

class BaseView(View):
    def get(self, request):
        return render(request, 'assistant/assistant-template.html', {'time':timezone.now()})