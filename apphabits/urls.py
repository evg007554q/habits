from django.urls import path


from apphabits.apps import ApphabitsConfig
from apphabits.views import habitsDestroyAPIView, habits_publicListAPIView, habitsListAPIView, habitsCreateAPIView, \
    habit_cartAPIView, habit_updateAPIView

app_name = ApphabitsConfig.name


urlpatterns = [
    path('habits/<int:pk>/delete/', habitsDestroyAPIView.as_view(), name='habits _delete'),
    path('habits/', habitsListAPIView.as_view(), name='habits_list'),
    path('habits_public/', habits_publicListAPIView.as_view(), name='habits_public_list'),
    path('habits/create/', habitsCreateAPIView.as_view(), name='habits_create'),
    path("habits/<int:pk>/detail/", habit_cartAPIView.as_view(), name='habit_cart'),
    path("habits/<int:pk>/update/", habit_updateAPIView.as_view(), name='habit_update')


              ]
