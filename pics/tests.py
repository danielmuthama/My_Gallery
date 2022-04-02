from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.

class ImageTestClass(TestCase):
    def setUp(self):
        self.pixel= Image(name = 'Pixel', 
                        description ='Portrait', 
                        image ='images/pixel.jpg',
                        upload_date ='2019-05-10 17:30:36.627472+03')

    def test_instance(self):
        self.assertTrue(isinstance(self.pixel,Image))

    def test_save_method(self):
        self.pixel.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        self.pixel.save_image()
        self.pixel.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.pixel= Image(name = 'Pixel', 
                        description ='Potrait', 
                        image ='images/pixel.jpg',
                        upload_date ='2019-05-10 17:30:36.627472+03',
                        category = 'Potraits')

        def test_instance(self):
        self.assertTrue(isinstance(self.pixel.category,Category))