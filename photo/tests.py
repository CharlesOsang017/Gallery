from django.test import TestCase
from .models import Location,Picture,Category

# Create your tests here.    
class CategoryTestClass(TestCase):
    def setUp(self):
        '''
        Method to be run in every beginning of the test
        '''
        self.sports= Category(category='sport')

    def test_instance(self):
        self.assertTrue(isinstance(self.sports,Category))

    def tearDown(self):
        '''
        Method to clear the test that has been done on category
        '''
        Category.objects.all().delete()

    def test_save_method(self):
        '''
        Method to save category
        
        '''
        self.sports.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category)>0)

    def test_delete_method(self):
        '''
        Method to delete the category
        '''
        self.sports.delete_category('sports')
        category = Category.objects.all()
        self.assertTrue(len(category)==0)

class LocationTestClass(TestCase):

    #set up method
    def setUp(self):
        '''
        Method to be run in every beginning of the test
        '''
        self.nairobi= Location(location='nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))

    def tearDown(self):
        '''
        Method to clear the test that has been done on location
        '''
        Location.objects.all().delete()

    def test_save_method(self):
        '''
        Method to save the location
        
        '''
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_method(self):
        '''
        Method to delete the location
        
        '''
        self.nairobi.delete_location('nairobi')
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)
