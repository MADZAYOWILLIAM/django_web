from django.urls import path
from .views import ResourceListView, ResourceCreateView, ResourceDeleteView

urlpatterns = [
    path('', ResourceListView.as_view(), name='resource_list'),
    path('upload/', ResourceCreateView.as_view(), name='resource_create'),
    path('<int:pk>/delete/', ResourceDeleteView.as_view(), name='resource_delete'),
]
