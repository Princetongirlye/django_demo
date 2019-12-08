from django.urls import path
from book_management_system import views,books_views, author_views


app_name = 'book_management_system'


urlpatterns = [
    path('', views.publisher_list),
    path(r'publisher', views.publisher_list),
    path(r'add_publisher', views.add_publisher),
    path(r'delete_publisher', views.delete_publisher),
    path(r'edit_publisher', views.edit_publisher),

    # 出版社相关
    path('books_list', books_views.books_list),
    path('add_book', books_views.add_book),
    path('delete_book', books_views.delete_book),
    path('edit_book', books_views.edit_book),

    # 作者相关的对应表
    path('authors_list', author_views.authors_list),
    path('add_author', author_views.add_author),
    path('delete_author', author_views.delete_author),
    path('edit_author', author_views.edit_author),

]