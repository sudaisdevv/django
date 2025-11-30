from django.urls import path
from .views import save_name,list_names,delete_name

urlpatterns = [
    path('save-name/', save_name, name='save_name'),
    path('list-names/', list_names, name='list_names'),
    path('delete-name/', delete_name, name='delete_name' )
]
 