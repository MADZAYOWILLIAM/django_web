from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.db import IntegrityError
from django.urls import reverse

from .models import Service, ServiceRequest
from .forms import ServiceRequestForm


class ServiceListView(ListView):
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'services'
    ordering = ['-created_at']

    def get_queryset(self):
        return Service.objects.filter(is_active=True).order_by(*self.ordering)


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'

    def get_queryset(self):
        return Service.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['has_requested'] = ServiceRequest.objects.filter(
                user=self.request.user,
                service=self.object,
            ).exists()
        return context


class ServiceRequestCreateView(LoginRequiredMixin, CreateView):
    model = ServiceRequest
    form_class = ServiceRequestForm
    template_name = 'services/service_apply.html'

    def dispatch(self, request, *args, **kwargs):
        self.service = get_object_or_404(Service, pk=kwargs.get('pk'), is_active=True)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service'] = self.service
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.service = self.service
        try:
            response = super().form_valid(form)
        except IntegrityError:
            messages.warning(self.request, f'You have already applied for {self.service.name}.')
            return redirect('service_detail', pk=self.service.pk)
        messages.success(self.request, f'Successfully applied for {self.service.name}!')
        return response

    def get_success_url(self):
        return reverse('service_detail', kwargs={'pk': self.service.pk})
