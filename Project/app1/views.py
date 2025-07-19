from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # List of (url, label) tuples for each learn_docxtpl endpoint
    links = [
        ('/learn_docxtpl/add_text/', 'Add Text'),
        ('/learn_docxtpl/add_paragraph/', 'Add Paragraph'),
        ('/learn_docxtpl/django_model_data_to_docx/', 'Django Model Data to Docx'),
        ('/learn_docxtpl/django_model_data_to_docx_table/', 'Django Model Data to Docx Table'),
        ('/learn_docxtpl/django_model_data_to_docx_table_with_image/', 'Django Model Data to Docx Table With Image'),
        ('/learn_docxtpl/onerow2images/', 'One Row 2 Images'),
        ('/learn_docxtpl/onerow2images_html/', 'One Row 2 Images HTML'),
        # Uncomment or add more as you add more endpoints
        # ('/learn_docxtpl/add_paragraph/', 'Add Paragraph'),
        # ('/learn_docxtpl/add_footer/', 'Add Footer'),
        # ('/learn_docxtpl/add_header/', 'Add Header'),
        # ('/learn_docxtpl/add_image/', 'Add Image'),
        # ('/learn_docxtpl/add_table/', 'Add Table'),
    ]
    html = "<h1>Learn docxtpl Examples</h1><ul>"
    for url, label in links:
        html += f'<li><a href="{url}">{label}</a></li>'
    html += "</ul>"
    return HttpResponse(html)