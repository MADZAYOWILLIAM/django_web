from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    if request.user.is_authenticated and request.user.is_admin():
        from django.shortcuts import redirect
        return redirect('admin_dashboard')
    
    context = {'user': request.user}
    if request.user.is_authenticated:
        from programs.models import Enrollment
        from events.models import Attendance
        context['enrolled_programs_count'] = Enrollment.objects.filter(user=request.user).count()
        context['registered_events_count'] = Attendance.objects.filter(user=request.user).count()
        
    return render(request, 'dashboard.html', context)
