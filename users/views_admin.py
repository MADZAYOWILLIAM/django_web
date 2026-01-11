from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import User

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin() or self.request.user.is_superuser)

class UserListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users_list'
    ordering = ['username']

class UserRoleUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = User
    fields = ['role']
    template_name = 'users/user_role_form.html'
    success_url = reverse_lazy('user_list')
    
    def form_valid(self, form):
        messages.success(self.request, f"Role updated for user {form.instance.username}")
        return super().form_valid(form)

class UserDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

from django.views.generic import TemplateView
from programs.models import Program
from events.models import Event
from resources.models import Resource

class AdminDashboardView(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'users/admin_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users_count'] = User.objects.count()
        context['programs_count'] = Program.objects.count()
        context['events_count'] = Event.objects.count()
        context['resources_count'] = Resource.objects.count()
        return context
