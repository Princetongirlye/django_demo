from django.urls import path
from book_management_system import views


app_name = 'book_management_system'


urlpatterns = [
    path('', views.publisher_list),
    path(r'publisher', views.publisher_list),
    path(r'add_publisher', views.add_publisher),
    path(r'delete_publisher', views.delete_publisher),
    path(r'edit_publisher', views.edit_publisher),
]