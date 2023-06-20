from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('autori-list/', views.AutoriListView.as_view(), name='autori'),
    path('autori-list/<int:pk>', views.AutoriDetailView.as_view(), name='autor'),
    path('vystavy-list/', views.VystavyListView.as_view(), name='vystavy'),
    path('vystavy-list/<int:pk>', views.VystavyDetailView.as_view(), name='vystava'),
    path('obrazy-list/', views.ObrazyListView.as_view(), name='obrazy'),
    path('obrazy-list/<int:pk>', views.ObrazyDetailView.as_view(), name='obraz')
]