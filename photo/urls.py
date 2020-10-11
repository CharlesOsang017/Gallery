from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name = 'index'),
    path('about/', views.about, name='about'),
    path('search/', views.search_results, name='search_results'),
    path('image/<int:image_id>', views.view_image,name='view_image'),
    path('category/<int:id>', views.category,name='category')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
