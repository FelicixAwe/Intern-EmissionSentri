from django.urls import path
from .views import EmissionListView

urlpatterns = [
    path('emissions/', EmissionListView.as_view(
        {'get': 'list', 'post': 'create'}), name='emission-list'),
    path('emissions/<int:pk>/', EmissionListView.as_view(
        {'delete': 'destroy'}), name='emission-detail'),
]
