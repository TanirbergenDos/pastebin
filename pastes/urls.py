from django.urls import path
from . import views

app_name = 'pastes'
urlpatterns = [
    path('', views.create_paste, name='create'),
    path('<slug:pk>', views.show_paste, name='show')
]
