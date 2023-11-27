from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.input_list, name='input_list'),
    path('search/', views.search, name='search'),
    path('search/confirm/', views.confirm, name='confirm'),
    path('search/duplication/', views.duplication, name='duplication'),
    path('search/none_user/', views.none_user, name='none_user')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)