from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from path.forms import SimpleForm
from path.models import Post


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = SimpleForm()    
        args = {
            'form': form,
        }
        return render(request, self.template_name, args)