
import cv2
import numpy as np
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.http import JsonResponse

from analyzer.utils import getOrientiation, analyzeHorizontalImage, analyzeVerticalImage
from config.settings import PDF_WIDTH, PDF_HEIGHT


class AnalizeImageView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        img_post = request.FILES.get('picture', False)

        if img_post:
            img_post.file.seek(0)
            img_buffer = np.asarray(bytearray(img_post.file.read()), dtype=np.uint8)
            picture = cv2.imdecode(img_buffer, cv2.IMREAD_GRAYSCALE)
            orientation_picture = getOrientiation(picture)

            if orientation_picture == 'horizontal':
                w, h = analyzeHorizontalImage(picture, PDF_HEIGHT, PDF_WIDTH)
                return JsonResponse({'status': 200, 'response': {'orientation': 'horizontal', 'width': w, 'height': h}})
            else:
                w, h = analyzeVerticalImage(picture, PDF_WIDTH, PDF_HEIGHT)
                return JsonResponse({'status': 200, 'response': {'orientation': 'vertical', 'width': w, 'height': h}})

        return JsonResponse({'status': 200, 'response':'Image empty'})
