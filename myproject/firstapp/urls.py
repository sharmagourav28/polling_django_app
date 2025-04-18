from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index page"),
    # path('',views.home,name='home page'),
    path("<int:poll_id>/", views.poll_detail, name="poll_detail"),
    path("<int:poll_id>/result/", views.poll_result, name="poll_result"),
]
