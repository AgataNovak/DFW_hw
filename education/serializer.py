from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from education.models import Course, Lesson, Subscription
from education.validators import LinkValidator


class CourseSerializer(ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"
        validators = [LinkValidator(field="description")]

    def get_is_subscribed(self, obj):
        request = self.context.get("request")
        if request.user.is_authenticated:
            return Subscription.objects.filter(user=request.user, course=obj).exists()
        return False


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [LinkValidator(field="description"), LinkValidator(field="link")]


class CourseDetailSerializer(ModelSerializer):
    lessons_quantity = SerializerMethodField()
    lessons = LessonSerializer(read_only=True)

    def get_lessons_quantity(self, course):
        return Lesson.objects.filter(course=course.id).count()

    class Meta:
        model = Course
        fields = ["title", "description", "lessons_quantity", "lessons"]
