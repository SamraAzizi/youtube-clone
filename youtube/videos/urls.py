from django.urls import path
from . import views 

app_name = 'videos'

urlpatterns = [
    path('upload/', views.video_upload, name='video_upload'),
    path('upload/submit/', views.video_detail, name='upload_submit'),

]