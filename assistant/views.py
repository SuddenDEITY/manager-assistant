from django.shortcuts import render
from django.views import View
from django.utils import timezone
from .models import Client
# Create your views here.

class BaseView(View):
    def get(self, request):
        clients = Client.objects.all()
        return render(request, 'assistant/assistant-template.html', {'clients':clients})