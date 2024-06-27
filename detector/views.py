from django.http import JsonResponse
from .forms import ImageUploadForm
from .utils import pipe_detection_algo
from PIL import Image
import numpy as np
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def detect_pipes(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            multiplier = form.cleaned_data['multiplier']
            image = Image.open(image)
            image_np = np.array(image.convert('L'))  # Convert to grayscale

            # Process the image and get the count of detected pipes
            _, pipe_count = pipe_detection_algo(image_np)

            # Multiply the detected pipe count by the provided numeric value
            result = pipe_count * multiplier

            return JsonResponse({'result': result})
        else:
            return JsonResponse({'error': 'Invalid form'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)
