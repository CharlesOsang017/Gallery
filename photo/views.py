import os
from django.conf import settings
from django.shortcuts import render
from django.templatetags.static import static
from .models import Picture, Location,Category
from django.http import HttpResponse, Http404


def index(request):
    '''
    Method to return all images, locations, categories
    '''
    images = Picture.objects.all()
    location = Location.objects.all()
    categories = Category.get_all_categories()
    context = {
        "images":images,
        "location":location,
        "categorie": categories,
    }
    
    return render(request, 'photo/index.html', context)

def search_results(request):
    '''
    Method to search by location or category
    '''
    if 'result' in request.GET and request.GET["result"]:
        search_term = request.GET.get("result")
        searched_images = Picture.search_by_category(search_term)
       
        message = f"{search_term}"
        return render(request, 'photo/search.html', {"message":message, "images":searched_images})
    elif 'result' in request.GET and request.GET["result"]:
        search_term = request.GET.get("result")
        searched_images = Picture.search_by_location(search_term)
        message = f"{search_term}"    

        return render(request, 'photo/search.html', {"message":message, "images":searched_images})
    else:
        message = "You haven't searched for any term"
        return render(request, 'photo/search.html', {"message":message})

def view_image(request,image_id):
    '''
    Method to get image by id
    '''
    try:
        image = Picture.objects.get(id =  image_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "photo/post.html", {"image":image})

def category(request, id):
    '''
    Method to search by images or category
    '''
    # categories = Category.get_all_categories()
    images = Image.objects.filter(category__id=id)
    context = {
        "categories":categories,
        "images":images
    }
    return render(request, 'category.html', context)

def about(request):
    '''
    Method to return about template
    '''
    return render(request, 'photo/about.html')
