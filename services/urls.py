from django.urls import path

from .views import ServiceListView, ServiceDetailView, ServiceRequestCreateView

urlpatterns = [
    path('', ServiceListView.as_view(), name='service_list'),
    path('<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('<int:pk>/apply/', ServiceRequestCreateView.as_view(), name='service_apply'),
]
