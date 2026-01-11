from django.urls import path
from .views import ProgramListView, ProgramDetailView, ProgramCreateView, ProgramUpdateView, ProgramDeleteView, ProgramEnrollView

urlpatterns = [
    path('', ProgramListView.as_view(), name='program_list'),
    path('create/', ProgramCreateView.as_view(), name='program_create'),
    path('<int:pk>/', ProgramDetailView.as_view(), name='program_detail'),
    path('<int:pk>/update/', ProgramUpdateView.as_view(), name='program_update'),
    path('<int:pk>/delete/', ProgramDeleteView.as_view(), name='program_delete'),
    path('<int:pk>/enroll/', ProgramEnrollView.as_view(), name='program_enroll'),
]
