from django.urls import path

from analyzer.views import AnalizeImageView

urls = [
    path('analyze/image', AnalizeImageView.as_view(), name='analyze_image'),
]