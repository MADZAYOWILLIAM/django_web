from django.urls import path
from .views import ProgramListView, ProgramDetailView

urlpatterns = [
    path('', ProgramListView.as_view(), name='program_list'),
    path('<int:pk>/', ProgramDetailView.as_view(), name='program_detail'),
]
