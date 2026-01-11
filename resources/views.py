from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Resource
from .forms import ResourceForm

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin()

class ResourceListView(ListView):
    model = Resource
    template_name = 'resources/resource_list.html'
    context_object_name = 'resources'
    ordering = ['-uploaded_at']

class ResourceCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Resource
    form_class = ResourceForm
    template_name = 'resources/resource_form.html'
    success_url = reverse_lazy('resource_list')

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)

class ResourceDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Resource
    template_name = 'resources/resource_confirm_delete.html'
    success_url = reverse_lazy('resource_list')
