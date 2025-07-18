from django.urls import path, include
from . import views

urlpatterns = [
    # path('basic/', views.basic_example, name='basic_example'),
    # path('advanced/', views.advanced_example, name='advanced_example'),
    path('add_text/', views.add_text, name='add_text'),
    path('add_paragraph/', views.add_paragraph, name='add_paragraph'),
    path('django_model_data_to_docx/', views.django_model_data_to_docx, name='django_model_data_to_docx'),
    # path('add_paragraph/', views.add_paragraph, name='add_paragraph'),
    # path('add_footer/', views.add_footer, name='add_footer'),
    # path('add_header/', views.add_header, name='add_header'),
    # path('add_image/', views.add_image, name='add_image'),
    # path('add_table/', views.add_table, name='add_table'),
]