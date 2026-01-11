from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Program, Enrollment
from .forms import ProgramForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.views import View

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin()

class ProgramCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'programs/program_form.html'
    success_url = reverse_lazy('program_list')

    def form_valid(self, form):
        form.instance.coordinator = self.request.user
        return super().form_valid(form)

class ProgramUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'programs/program_form.html'
    success_url = reverse_lazy('program_list')

class ProgramDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Program
    template_name = 'programs/program_confirm_delete.html'
    success_url = reverse_lazy('program_list')

class ProgramListView(ListView):
    model = Program
    template_name = 'programs/program_list.html'
    context_object_name = 'programs'
    ordering = ['-start_date']


class ProgramDetailView(DetailView):
    model = Program
    template_name = 'programs/program_detail.html'
    context_object_name = 'program'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['is_enrolled'] = Enrollment.objects.filter(
                user=self.request.user, 
                program=self.object
            ).exists()
        return context

class ProgramEnrollView(LoginRequiredMixin, View):
    def post(self, request, pk):
        program = get_object_or_404(Program, pk=pk)
        
        # Check if already enrolled
        if Enrollment.objects.filter(user=request.user, program=program).exists():
            messages.warning(request, f'You are already enrolled in {program.title}.')
        else:
            Enrollment.objects.create(user=request.user, program=program)
            messages.success(request, f'Successfully enrolled in {program.title}!')
            
        return redirect('program_detail', pk=pk)
