from django.shortcuts import render
import easyocr
import matplotlib.pyplot as plt
# Create your views here.
from django.http import JsonResponse
import cv2
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
from .forms import RegistrationForm, StudentForm
from .models import Person, Student

def index(request):
    return render(request, 'index.html')


@csrf_exempt
def capture_image(request):
    if request.method == 'POST':
        image_data_url = request.POST.get('image_data', '')
        reader = easyocr.Reader(['en'])
        # Extract base64 image data
        image_data = image_data_url.split(',')[1]
        
        # Convert base64 to binary
        binary_image = np.frombuffer(base64.b64decode(image_data), dtype=np.uint8)
        
        # Decode binary image to OpenCV image
        opencv_image = cv2.imdecode(binary_image, cv2.IMREAD_COLOR)
        
        # Do something with the OpenCV image (e.g., save to disk)
        cv2.imwrite('C:/Users/admin/Documents/django_project/webcam_project/captureimage/captured_image.png', opencv_image)
        # Perform OCR on the image
    result = reader.readtext(opencv_image)

    # Display the original image
    plt.imshow(cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

    # Display the extracted text and its bounding boxes
    for detection in result:
        text = detection[1]
        bbox = detection[0]
        print(f'Text: {text}, Bounding Box: {bbox}')
        return JsonResponse({'message': 'Image captured successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        student_form = StudentForm(request.POST)
        if form.is_valid() and student_form.is_valid():
            user = form.save()
            person = Person.objects.create(
                user=user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email']
            )
            student = Student.objects.create(
                person=person,
                student_id=student_form.cleaned_data['student_id'],
                grade=student_form.cleaned_data['grade']
            )
            return redirect('success')
    else:
        form = RegistrationForm()
        student_form = StudentForm()

    return render(request, 'registration/register.html', {'form': form, 'student_form': student_form})

def registration_success(request):    