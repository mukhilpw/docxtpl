from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from docxtpl import DocxTemplate
import inspect
import os



def download_file(request, context, file_path, current_function_name):
    doc = DocxTemplate(f"learn_docxtpl/input/{current_function_name}.docx")
    doc.render(context)
    output_path = f"learn_docxtpl/output/{current_function_name}.docx"
    doc.save(output_path)
    with open(output_path, "rb") as f:
        file_data = f.read()
        if file_data:
            response = HttpResponse(file_data, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = f'attachment; filename={current_function_name}.docx'
            return response
        else:
            return HttpResponse(b"File could not be downloaded.", status=500)


def add_text(request):
    frame = inspect.currentframe()
    current_function_name = frame.f_code.co_name if frame is not None else "unknown"
    context = {
        'data': f'this is for testing {current_function_name}',
        'name': 'John Doe',
        'age': 30,
    }
    file = download_file(request, context, f"learn_docxtpl/output/{current_function_name}.docx", current_function_name)
    return file



def add_paragraph(request):
    frame = inspect.currentframe()
    current_function_name = frame.f_code.co_name if frame is not None else "unknown"
    paragraph = """
This is the first line of a sample paragraph.\n Here is the second line, dfhhh kjhkjdf jkhjkd shfkjhsdkfjh dskfhksjdfh kjproviding more detail.The third line continues the explanation further.\n
On the fourth line, we add additional context.\n
The fifth line helps to wrap up the main idea.\n
Finally, the sixth line concludes this sample paragraph.
    """
    context = {
        'data': f'this is for testing {current_function_name}',
        'paragraph': paragraph,
    }
    return download_file(request, context, f"learn_docxtpl/output/{current_function_name}.docx", current_function_name)

# django model data to docx
from learn_docxtpl.models import BookDetails
def django_model_data_to_docx(request):
    frame = inspect.currentframe()
    current_function_name = frame.f_code.co_name if frame is not None else "unknown"

    book_details = BookDetails.objects.all()
    print(book_details)
    # INSERT_YOUR_CODE
    # Get all field names of BookDetails model
    field_names = [
        field.name 
        for field in BookDetails._meta.get_fields()
    ]
    # INSERT_YOUR_CODE
    # Get all data from BookDetails as list of dicts
    data = list(book_details.values())
    print("Data:", data)
    print("Field names:", field_names)
    # return HttpResponse(f"all fiels name {field_names}all data {data}""")
    context = {
        'data': f'this is for testing {current_function_name}',
        'book_table': data,
        'field_names': field_names,
    }
    return download_file(request, context, f"learn_docxtpl/output/{current_function_name}.docx", current_function_name)










# def add_paragraph(request): 
#     doc = DocxTemplate("learn_docxtpl/templates/add_paragraph.docx")
#     context = {
#         'name': 'John Doe',
#         'age': 30,
#     }
#     doc.render(context)
#     output_path = "learn_docxtpl/output/add_paragraph.docx"
#     doc.save(output_path)
#     with open(output_path, "rb") as f:
#         response = HttpResponse(f.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#         response['Content-Disposition'] = 'attachment; filename=add_paragraph.docx'
#         return response

# def add_footer(request):
#     doc = DocxTemplate("learn_docxtpl/templates/add_footer.docx")
#     context = {
#         'name': 'John Doe',
#         'age': 30,
#     }
#     doc.render(context)
#     output_path = "learn_docxtpl/output/add_footer.docx"
#     doc.save(output_path)
#     with open(output_path, "rb") as f:
#         response = HttpResponse(f.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#         response['Content-Disposition'] = 'attachment; filename=add_footer.docx'
#         return response
    
# def add_header(request):
#     doc = DocxTemplate("learn_docxtpl/templates/add_header.docx")
#     context = {
#         'name': 'John Doe',
#         'age': 30,
#     }
#     doc.render(context)
#     output_path = "learn_docxtpl/output/add_header.docx"
#     doc.save(output_path)
#     with open(output_path, "rb") as f:
#         response = HttpResponse(f.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#         response['Content-Disposition'] = 'attachment; filename=add_header.docx'
#         return response

# def add_image(request):
#     doc = DocxTemplate("learn_docxtpl/templates/add_image.docx")
#     context = {
#         'name': 'John Doe',
#         'age': 30,
#     }
#     doc.render(context)
#     output_path = "learn_docxtpl/output/add_image.docx"
#     doc.save(output_path)
#     with open(output_path, "rb") as f:
#         response = HttpResponse(f.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#         response['Content-Disposition'] = 'attachment; filename=add_image.docx'
#         return response

# def add_table(request):
#     doc = DocxTemplate("learn_docxtpl/templates/add_table.docx")
#     context = {
#         'name': 'John Doe',
#         'age': 30,
#     }
#     doc.render(context)
#     output_path = "learn_docxtpl/output/add_table.docx"
#     doc.save(output_path)
#     with open(output_path, "rb") as f:
#         response = HttpResponse(f.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#         response['Content-Disposition'] = 'attachment; filename=add_table.docx'
#         return response



