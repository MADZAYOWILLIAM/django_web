from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Event, Attendance
from .forms import EventForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.views import View

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin()

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['registered_event_ids'] = list(Attendance.objects.filter(
                user=self.request.user
            ).values_list('event_id', flat=True))
        return context

class EventRegisterView(LoginRequiredMixin, View):
    def post(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        
        if Attendance.objects.filter(user=request.user, event=event).exists():
            messages.warning(request, f'You are already registered for {event.title}.')
        else:
            Attendance.objects.create(user=request.user, event=event)
            messages.success(request, f'Successfully registered for {event.title}!')
            
        return redirect('event_list')

class EventCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event_list')

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event_list')

class EventDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('event_list')
