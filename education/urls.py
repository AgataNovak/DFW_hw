from rest_framework.routers import SimpleRouter

from education.apps import EducationConfig

from .views import (CourseViewSet, LessonViewSet)

appname = EducationConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)
router.register("", LessonViewSet)

urlpatterns = [] + router.urls
