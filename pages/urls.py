from django.urls import path
from .views import IndexView, TourView, AgentView, TourDetailView, AgentDetailView, TourCreateView, TourUpdateView, TourDeleteView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tour/', TourView.as_view(), name='tour'),
    path('tour_detail/<int:pk>/', TourDetailView.as_view(), name='tour_detail'),
    path("tour/create/", TourCreateView.as_view(), name='tour_create'),
    path("tour/<int:pk>/update/", TourUpdateView.as_view(), name='tour_update'),
    path("tour/<int:pk>/delete/", TourDeleteView.as_view(), name='tour_delete'),
    path('agent/', AgentView.as_view(), name='agent'),
    path('agent_detail/<int:pk>/', AgentDetailView.as_view(), name='agent_detail'),
]
