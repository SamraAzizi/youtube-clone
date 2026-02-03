from django.db import models
from django.contrib.auth.models import User
from .imagekit_client import (
    get_optimized_video_url, get_streaming_video_url, get_imagekit_client, get_image_watermark
)


class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)


    file_id = models.CharField(max_length=255, unique=True)
    video_url = models.URLField(max_length=500)
    thumbnail_url = models.URLField(max_length=500, blank=True)

    view = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def display_thumbnail_url(self):
        if self.thumbnail_url and "/thumbnail/" in self.thumbnail_url:
            return get_image_watermark(self.thumbnail_url, username=self.user.username)
        return self.generated_thumbnail_url()
    
    @property
    def generated_thumbnail_url(self):
        if not self.file_id:
            return ""
        return get_thumbnail_url(self.video_url)
    
    @property
    def streaming_url(self):
        if not self.video_url:
            return ""
        return get_streaming_video_url(self.video_url)
    
    @property
    def optimized_url(self):
        if not self.video_url:
            return ""
        return get_optimized_video_url(self.video_url)
    
class VideoLike(models.Model):
    LIKE = 1
    DISLIKE = -1
    LIKE_CHOICES = [
        (LIKE, "Like"),
        (DISLIKE, "Dislike"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='likes_dislikes')
    value = models.SmallIntegerField(choices=LIKE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'video']

    def __str__(self):
        action = "Liked" if self.value == self.LIKE else "Disliked"
        return f"{self.user.username} {action} {self.video.title}"