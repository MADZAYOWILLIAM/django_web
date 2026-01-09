from django.views.generic import ListView
from django.contrib.auth import get_user_model

User = get_user_model()

class MentorshipListView(ListView):
    model = User
    template_name = 'mentorship/mentorship_list.html'
    context_object_name = 'mentors'

    def get_queryset(self):
        return User.objects.filter(role=User.Role.MENTOR)
