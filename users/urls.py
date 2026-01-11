from django.urls import path
from . import views
from . import views_admin

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('manage/', views_admin.UserListView.as_view(), name='user_list'),
    path('manage/<int:pk>/role/', views_admin.UserRoleUpdateView.as_view(), name='user_role_update'),
    path('manage/<int:pk>/delete/', views_admin.UserDeleteView.as_view(), name='user_delete'),
    path('dashboard/', views_admin.AdminDashboardView.as_view(), name='admin_dashboard'),
]
