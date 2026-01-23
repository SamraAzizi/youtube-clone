from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import Video
from .forms import VideoUploadForm
from .imagekit_client import upload_video, upload_thumbnail


# Create your views here.


@login_required
@require_POST
def video_upload(request):
    form = VideoUploadForm(request.POST, request.FILES)
    if form.is_valid():
        video_file = form.cleaned_data['video_file']
        custom_thumbnail = request.POST.get('thumbnail_data', "")


        try:
            result = upload_video(
                file_data=video_file.read(),
                file_name=video_file.name
            )