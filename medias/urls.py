from django.urls import path
from .views import (
    PhotoDetail,
    GetRoomUploadURL,
    UploadRoomPhoto,
    GetExperienceUploadURL,
    UploadExperiencePhoto,
)

urlpatterns = [
    path("photos/get-room-url", GetRoomUploadURL.as_view()),
    path("photos/upload-room-photo", UploadRoomPhoto.as_view()),
    path("photos/<int:pk>", PhotoDetail.as_view()),
    path("photos/get-experience-url", GetExperienceUploadURL.as_view()),
    path("photos/upload-experience-photo", UploadExperiencePhoto.as_view()),
]
