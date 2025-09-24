from django.shortcuts import render, redirect
from django.views import View
from .models import Response
from .forms import ResponseForm

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/index.html')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            response = ResponseForm(request.POST)
            if response.is_valid():
                answer = response.cleaned_data['answer']
                if answer == 1:
                    response.save()
                    return redirect('FAR') # FAR == First Answer Render
        else:
            response = ResponseForm()
        return render(request, 'core/index.html')

class FirstAnswer(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/adding-page.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'core/adding-page.html')