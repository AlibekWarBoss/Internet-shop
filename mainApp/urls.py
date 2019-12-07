from django.conf.urls import url
from . import views
from django.urls import include, path

app_name = "a"

urlpatterns = [
    path('', views.index, name='index'),
    path('laptop/', views.laptop, name = 'laptop'),
    path('smartphone/', views.smartphone, name = 'smartphone'),
    path('camera/', views.camera, name = 'camera'),
    path('earphone/', views.earphone, name = 'earphone'),
    # path('(^?<laptop_name>[\w-]+)/',views.laptop_detail, name = "laptop_detail"),
    path('(^?<camera_name>[\w-]+)/',views.camera_detail, name = "camera_detail"),
    path('(^?<smartphone_name>[\w-]+)/',views.smartphone_detail, name = "smartphone_detail"),
    path('(^?<earphone_name>[\w-]+)/',views.earphone_detail, name = "earphone_detail"),

]
