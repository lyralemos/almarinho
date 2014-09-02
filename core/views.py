from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView

from models import Entry

class EntryListView(ListView):
    model = Entry
    template_name = "core/index.html"
    paginate_by = 10

    def get_queryset(self):
    	return Entry.objects.filter(status='published').order_by('-data_publicacao')

class EntryDetailView(DetailView):
	model = Entry
	template_name = 'core/detail.html'