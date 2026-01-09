from django.views.generic import ListView, DetailView
from .models import Program

class ProgramListView(ListView):
    model = Program
    template_name = 'programs/program_list.html'
    context_object_name = 'programs'
    ordering = ['-start_date']

class ProgramDetailView(DetailView):
    model = Program
    template_name = 'programs/program_detail.html'
    context_object_name = 'program'
