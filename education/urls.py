from django.urls import path
from rest_framework.routers import SimpleRouter

from education.apps import EducationConfig

from .views import (CourseViewSet,
                    LessonCreateAPIView,
                    LessonListAPIView,
                    LessonUpdateAPIView,
                    LessonRetrieveAPIView,
                    LessonDestroyAPIView, SubscriptionView)

app_name = EducationConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListAPIView.as_view(), name="lessons_list"),
    path("lessons/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lessons_retrieve"),
    path("lessons/create/", LessonCreateAPIView.as_view(), name="lessons_create"),
    path(
        "lessons/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lessons_update"
    ),
    path(
        "lessons/<int:pk>/delete/",
        LessonDestroyAPIView.as_view(),
        name="lessons_delete",
    ),
    path("subscription/", SubscriptionView.as_view(), name="subscription"),
]

urlpatterns += router.urls
