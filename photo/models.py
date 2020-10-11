from django.db import models
import datetime as dt

class Picture(models.Model):
    title = models.CharField(max_length =30)
    image = models.ImageField(upload_to = 'images/', default="")
    posted_date= models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length =200)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    
    class Meta:
        '''
        class method to display images by date posted
        '''
        ordering = ['posted_date']

    def __str__(self):
        return self.description

    @classmethod
    def search_by_category(cls, search_term):
        '''
        Method to filter images by category
        '''
        result = cls.objects.filter(category__category__icontains=search_term)
        return result 

    def search_by_location(cls, search_term):
        '''
        Method to filter images by location
        '''
        result = cls.objects.filter(location__location__icontains=search_term)
        return result

class Category(models.Model):
    category = models.CharField(max_length =30)

    @classmethod
    def get_all_categories(cls):
        '''
        Method to get all categories
        '''
        categories = cls.objects.all()
        return categories

    def save_category(self):
        '''
        Method to save category
        '''
        self.save()

    @classmethod
    def delete_category(cls,category):
        cls.objects.filter(category=category).delete()

    
    def __str__(self):
        return self.category


class Location(models.Model):
    location = models.CharField(max_length =30)

    @classmethod
    def get_all_locations(cls):
        '''
        Method to get all locations
        '''
        locations = cls.objects.all()
        return locations

    def save_location(self):
        '''
        Method to save location
        '''
        self.save()

    # def delete_location(self):
    #     '''
    #     Method to delete location
    #     '''
    #     self.delete()
    @classmethod
    def delete_location(cls,location):
        cls.objects.filter(location=location).delete()

    
    def __str__(self):
        return self.location