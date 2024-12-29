from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("education/", include(("education.urls", "education"), namespace="education")),
    path("users/", include("users.urls", namespace="users")),
]

