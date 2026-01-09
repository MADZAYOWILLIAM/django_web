from django.urls import path
from .views import MentorshipListView

urlpatterns = [
    path('', MentorshipListView.as_view(), name='mentorship_list'),
]
