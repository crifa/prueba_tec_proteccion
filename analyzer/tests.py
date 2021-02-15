from django.core.files import File
from django.test import TestCase
import json

from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile


class AnalyzeImageTestCase(TestCase):

    def test_analyze_image_horizontal(self):
        print("***** horizontal test *****")
        file_list = ['ex1.jpg', 'ex2.jpg', 'ex3.jpg']
        filename = file_list[0]
        file = File(open('media/testfiles/horizontal/'+filename, 'rb'))
        uploaded_file = SimpleUploadedFile(filename, file.read(), content_type='multipart/form-data')
        url = '/analyze/image'
        client = APIClient()
        response = client.post(url, {'picture': uploaded_file}, format='multipart')
        print(response.content)
        self.assertEqual(response.status_code, 200)

    def test_analyze_image_vertical(self):
        print("***** vertical test *****")
        file_list = ['ex4.jpg', 'ex5.jpg', 'ex6.jpg']
        filename = file_list[0]
        file = File(open('media/testfiles/vertical/'+filename, 'rb'))
        uploaded_file = SimpleUploadedFile(filename, file.read(), content_type='multipart/form-data')
        url = '/analyze/image'
        client = APIClient()
        response = client.post(url, {'picture': uploaded_file}, format='multipart')
        print(response.content)
        self.assertEqual(response.status_code, 200)

