
from django.urls import path
from . import views
urlpatterns = [
    path('', views.EventsListView.as_view(), name="home"),
    path('event/<int:pk>/', views.EventDetailView.as_view(), name="events-detail"),
    path('event/create/', views.EventCreateView.as_view(), name="event-create"),
    path('event/<int:pk>/update', views.EventUpdateView.as_view(), name="events-update"),
    path('event/<int:pk>/delete', views.EventDeleteView.as_view(), name="events-delete"),
    #path('event/<int:pk>/category/<int:pk>', views.CategoryDetailView.as_view(), name="caegory-detail"),
    path('event/<int:pk>/category/', views.CategoryCreateView.as_view(), name='add_category'),
    path('category/<int:pk>/slot', views.SlotCreateView.as_view(), name='add_slot'),
    path('about/', views.about,name="about"),
]
