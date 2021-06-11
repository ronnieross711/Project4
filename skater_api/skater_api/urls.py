from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('skaters/', views.SkaterList.as_view(), name='skater_list'),
    path('skaters/<int:pk>', views.SkaterDetail.as_view(), name='skater_detail'),
    path('tricks/', views.TricksList.as_view(), name='trick_list'),
    path('tricks/<int:pk>', views.TricksDetail.as_view(), name='trick_detail'),
]