from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from docxtpl import DocxTemplate
import inspect
import os
from django.conf import settings
from django.conf import settings



def download_file(request, context, file_path, current_function_name):
    doc = DocxTemplate(f"learn_docxtpl/input/{current_function_name}.docx")
    # # Handle image path if present in context
    # if 'image_path' in context:
    #     from docxtpl import InlineImage
    #     from docx.shared import Mm
    #     context['image'] = InlineImage(doc, image_descriptor=context['image_path'], width=Mm(20), height=Mm(10))
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
from learn_docxtpl.models import BookDetails, BookImage, BookImage
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



def django_model_data_to_docx_table(request):
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


from docxtpl import InlineImage
from docx.shared import Mm

def django_model_data_to_docx_table_with_image(request):
    frame = inspect.currentframe()
    current_function_name = frame.f_code.co_name if frame is not None else "unknown"
    book_details = BookDetails.objects.all()
    book_images = BookImage.objects.all()
    print(book_details)

    # INSERT_YOUR_CODE
    # Get all field names of BookImage model
    field_names = [
        field.name 
        for field in BookImage._meta.get_fields()
    ]
    # INSERT_YOUR_CODE
    # Get all data from BookImage as list of dicts
    data = list(book_images.values())
    print("Data:", data)
    print("Field names:", field_names)
    # Create the document template first
    doc = DocxTemplate(f"learn_docxtpl/input/{current_function_name}.docx")
    
    # Process images for all BookImage records
    processed_data = []
    for book_image in data:
        book_image_dict = dict(book_image)
        if book_image.get('image2'):
            # Get the full path to the image file
            image_file_path = os.path.join(settings.BASE_DIR, book_image['image2'])
            if os.path.exists(image_file_path):
                book_image_dict['image_obj'] = InlineImage(doc, image_descriptor=image_file_path, width=Mm(60), height=Mm(40))
            else:
                book_image_dict['image_obj'] = None
        else:
            book_image_dict['image_obj'] = None
        processed_data.append(book_image_dict)
    
    def group_images(images, n=2):
        return [images[i:i + n] for i in range(0, len(images), n)]

    book_images_rows = group_images(processed_data, 2)
    context = {
        'data': f'this is for testing {current_function_name}',
        'book_images_table': processed_data,
        'field_names': field_names,
        'book_images_rows': book_images_rows,
    }

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
    # return download_file(request, context, f"learn_docxtpl/output/{current_function_name}.docx", current_function_name)



def group_images(images, n=2):
    # INSERT_YOUR_CODE
    # one by one code
    # This function groups the images list into sublists of length n
    # For example, if images = [1,2,3,4,5] and n=2, result: [[1,2],[3,4],[5]]
    # The return statement below does this using list slicing in a loop
    # INSERT_YOUR_CODE
    grouped = []
    for i in range(0, len(images), n):
        group = images[i:i + n]
        print(f"Group: {group}")
        grouped.append(group)
    return grouped
    # return [images[i:i + n] for i in range(0, len(images), n)]

def onerow2images(request):
    frame = inspect.currentframe()
    current_function_name = frame.f_code.co_name if frame is not None else "unknown"
    doc = DocxTemplate(f"learn_docxtpl/input/{current_function_name}.docx")
    
    # Get all BookImage records
    # book_images = BookImage.objects.all()
    book_images = BookImage.objects.filter(book__id=2)
    print(f"Found {book_images.count()} book images")
    
    # Process images for display
    processed_data = []
    for book_image in book_images:
        if book_image.image2:
            # Get the full path to the image file
            image_file_path = os.path.join(settings.BASE_DIR, book_image.image2.name)
            print(f"Image path: {image_file_path}")
            if os.path.exists(image_file_path):
                processed_data.append({
                    'image_obj': InlineImage(doc, image_descriptor=image_file_path, width=Mm(90), height=Mm(60)),
                    'book_id': book_image.book.id,
                    'book_title': book_image.book.title
                })
                print(f"Added image for book: {book_image.book.title}")
            else:
                print(f"Image file not found: {image_file_path}")
    print(f"Processed data: {processed_data}")
    # Group images into rows of 2
    book_images_rows = group_images(processed_data, 2)
    print(f"Created {len(book_images_rows)} rows of images")
    
    context = {
        'data': f'this is for testing {current_function_name}',
        'book_images_rows': book_images_rows,
        'total_images': len(processed_data),
        'processed_data': processed_data,
    }
    # print(f"Context: {context}")

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


def onerow2images_html(request):
    frame = inspect.currentframe()
    current_function_name = frame.f_code.co_name if frame is not None else "unknown"
    
    # Get all BookImage records
    # book_images = BookImage.objects.all()
    book_images = BookImage.objects.filter(book__id=2)
    print(f"Found {book_images.count()} book images")
    
    # Process images for HTML display
    processed_data = []
    for book_image in book_images:
        if book_image.image2:
            # For HTML, we need the URL path, not the file path
            image_url = book_image.image2.url if book_image.image2 else None
            if image_url:
                processed_data.append({
                    'image_url': image_url,
                    'book_id': book_image.book.id,
                    'book_title': book_image.book.title
                })
                print(f"Added image for book: {book_image.book.title}")
                print(f"Image URL: {image_url}")
            else:
                print(f"No URL for image: {book_image.image2}")
        else:
            print(f"No image2 field for book_image: {book_image.id}")
    
    # Group images into rows of 2
    book_images_rows = group_images(processed_data, 2)
    print(f"Created {len(book_images_rows)} rows of images")
    
    context = {
        # 'data': f'this is for testing {current_function_name}',
        'book_images_rows': book_images_rows,
        # 'total_images': len(processed_data)
    }
    print(f"Context: {context}")
    return render(request, 'onerow2images_html.html', context)

def test_image_paths_simple(request):
    """Simple test to check image paths"""
    book_images = BookImage.objects.all()
    
    result = []
    for book_image in book_images:
        if book_image.image2:
            # Check both file path and URL
            file_path = os.path.join(settings.BASE_DIR, book_image.image2.name)
            file_exists = os.path.exists(file_path)
            url_path = book_image.image2.url if book_image.image2 else None
            
            result.append({
                'id': book_image.id,
                'book_title': book_image.book.title,
                'image_name': book_image.image2.name,
                'file_path': file_path,
                'file_exists': file_exists,
                'url_path': url_path
            })
    
    return HttpResponse(f"<h1>Image Path Test</h1><pre>{result}</pre>")


