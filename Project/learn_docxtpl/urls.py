from django.urls import path, include
from . import views

urlpatterns = [
    # path('basic/', views.basic_example, name='basic_example'),
    # path('advanced/', views.advanced_example, name='advanced_example'),
    path('add_text/', views.add_text, name='add_text'),
    path('add_paragraph/', views.add_paragraph, name='add_paragraph'),
    path('django_model_data_to_docx/', views.django_model_data_to_docx, name='django_model_data_to_docx'),
    path('django_model_data_to_docx_table/', views.django_model_data_to_docx_table, name='django_model_data_to_docx_table'),
    path('django_model_data_to_docx_table_with_image/', views.django_model_data_to_docx_table_with_image, name='django_model_data_to_docx_table_with_image'),
    # path('test_image_paths/', views.test_image_paths, name='test_image_paths'),
    # path('books_with_images/', views.books_with_images, name='books_with_images'),
    path('onerow2images/', views.onerow2images, name='onerow2images'),
    path('onerow2images_html/', views.onerow2images_html, name='onerow2images_html'),
    path('test_image_paths_simple/', views.test_image_paths_simple, name='test_image_paths_simple'),
    
    # path('add_paragraph/', views.add_paragraph, name='add_paragraph'),
    # path('add_footer/', views.add_footer, name='add_footer'),
    # path('add_header/', views.add_header, name='add_header'),
    # path('add_image/', views.add_image, name='add_image'),
    # path('add_table/', views.add_table, name='add_table'),
]