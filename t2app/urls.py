from django.urls import path
from t2app import views

urlpatterns = [
    # path('filter/', views.filter_boxes, name='filter_boxes'),
    # path('about',views.about),
    # path('abt',views.abt),
    path('all', views.all), 
    path('catfilter/<cv>',views.catfilter), 
    path('locfilter/<vc>',views.locfilter),
    path('search',views.search),
]
