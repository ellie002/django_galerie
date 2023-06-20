from django.shortcuts import render
from .models import Vystava, Obrazy, Autori, Mistnosti
from django.views.generic import ListView, DetailView

def index(request):
    context = {
        'autori': Autori.objects.order_by('prijmeni')[:3],
        'obrazy': Obrazy.objects.order_by('nazev')[:3]
    }
    return render(request, "index.html", context=context)

class AutoriListView(ListView):
    model = Autori
    context_object_name = 'autori'
    template_name = 'autori/autori_list.html'

class AutoriDetailView(DetailView):
    model = Autori
    context_object_name = 'autor'
    template_name = 'autori/autori_detail.html'

class VystavyListView(ListView):
    model = Vystava
    context_object_name = 'vystavy'
    template_name = 'vystavy/vystavy_list.html'

class VystavyDetailView(DetailView):
    model = Vystava
    context_object_name = 'vystava'
    template_name = 'vystavy/vystavy_detail.html'

class ObrazyListView(ListView):
    model = Obrazy
    context_object_name = 'obrazy'
    template_name = 'obrazy/obrazy_list.html'

class ObrazyDetailView(DetailView):
    model = Obrazy
    context_object_name = 'obraz'
    template_name = 'obrazy/obrazy_detail.html'