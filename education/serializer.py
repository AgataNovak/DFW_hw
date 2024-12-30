from rest_framework.serializers import ModelSerializer, SerializerMethodField

from education.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    lessons_quantity = SerializerMethodField()
    lessons = LessonSerializer(read_only=True)

    def get_lessons_quantity(self, course):
        return Lesson.objects.filter(course=course.id).count()

    class Meta:
        model = Course
        fields = ["title", "description", "lessons_quantity", "lessons"]


class LessonDetailSerializer(ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ["title", "description",]
