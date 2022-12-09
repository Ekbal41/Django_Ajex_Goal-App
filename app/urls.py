from django.urls import path, include
from .views import form_submit, get_data, delete_goal

urlpatterns = [
    
    path('', form_submit, name='form_submit' ),
    path('get_data',get_data, name='get_data' ),
    path('delete_goal/<str:id>',delete_goal, name='delete_goal' )
]