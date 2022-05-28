from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.landing),
    path('home', views.home_view),
    path('about', views.about),
    path('genre/<str:genre>', views.iteration_view)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
