from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('gallery', views.index2, name='gallery'),
    path('about', views.index4, name='about'),
    path('news', views.index3, name='news'),
    path('timetable', views.index5, name='timetable'),
    path('write', views.write, name='write'),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    