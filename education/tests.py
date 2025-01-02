from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from users.models import User
from education.models import Course, Lesson


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="gorskaia_agata@example.com")
        self.course = Course.objects.create(
            title="Test Course Title", description="Test Course Description", owner=self.user
        )
        self.client.force_authenticate(user=self.user)

        def test_lesson_create(self):
            data = {
                'title': 'Test title',
                'description': 'Test description',
                'course': self.course,
                'owner': self.user
            }
            self.lesson = Lesson.objects.create(
                title="Test Lesson Title",
                description="Test Lesson Description",
                course=self.course,
                owner=self.user,
            )
            response = self.client.post(
                '/lessons/create/',
                data=data
            )
            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK
            )

        def test_lesson_retrieve(self):
            url = reverse(
                "education:lessons_retrieve",
                args=(self.lesson.pk,)
            )
            response = self.client.get(url)
            data = response.json()
            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK
            )
            self.assertEqual(
                data.get("name"),
                self.lesson.name
            )

        def test_lesson_delete(self):
            url = reverse(
                "education:lessons_delete",
                args=(self.lesson.pk,)
            )
            response = self.client.delete(url)
            self.assertEqual(
                response.status_code,
                status.HTTP_204_NO_CONTENT
            )
            self.assertEqual(
                Lesson.objects.all().count(),
                0
            )

        def test_lesson_update(self):
            url = reverse(
                "education:lessons_update",
                args=(self.lesson.pk,)
            )
            data = {
                "title": "Test lesson",
                "description": "Test lesson description",
                "link": "https://www.youtube.com",
                "course": self.course.pk,
                "owner": self.user
            }
            response = self.client.patch(url, data)
            data = response.json()
            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK
            )
            self.assertEqual(
                data.get("title"),
                "Test lesson"
            )
