from django.http import JsonResponse
from .forms import ImageUploadForm
from .utils import pipe_detection_algo
from PIL import Image
import numpy as np
from django.views.decorators.csrf import csrf_exempt
import base64
import cv2

@csrf_exempt
def detect_pipes(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            image = Image.open(image)
            image_np = np.array(image.convert('L'))  # Convert to grayscale

            output_image, pipe_count = pipe_detection_algo(image_np)

            _, buffer = cv2.imencode('.png', output_image)  # Encode image to PNG
            img_str = base64.b64encode(buffer).decode('utf-8')  # Convert to base64 string

            return JsonResponse({'result': pipe_count, 'image': img_str})
        else:
            return JsonResponse({'error': 'Invalid form'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)