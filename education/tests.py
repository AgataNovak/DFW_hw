from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from users.models import User
from education.models import Course, Lesson, Subscription


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="Gorskaia_agata@example.com")
        self.course = Course.objects.create(
            title="Test Course Title",
            description="Test Course Description",
            owner=self.user
        )
        self.client.force_authenticate(user=self.user)
        self.lesson = Lesson.objects.create(
            title="Test Lesson Title",
            description="Test Lesson Description",
            link=None,
            course=self.course,
            owner=self.user
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
            data.get("title"),
            self.lesson.title
        )

    def test_lesson_update(self):
        url = reverse(
            "education:lessons_update",
            args=(self.lesson.pk,)
        )
        data = {
            "title": "test postman updated",
            "description": "i am testing postman at this moment"
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("title"),
            "test postman updated"
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

    def test_lesson_create(self):
        data = {
            'title': 'test title lesson 1',
            'description': 'test description lesson 1',
            'course': self.course,
        }
        url = reverse(
            "education:lessons_create"
        )
        response = self.client.post(url, data=data)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        data = response.json()
        self.assertEqual(
            data.get("title"),
            "test title lesson 1"
        )


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="Gorskaia_Agatha@example.com")

        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            title="Test Course Title for sub",
            description="Test Course Description for sub",
            owner=self.user
        )

    def test_subscription_create(self):
        url = reverse(
            "education:subscription"
        )
        data = {
            "course_id": self.course.pk,
            "user": self.user
        }
        response = self.client.post(url, data=data)
        data = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            data,
            {'message': "Подписка добавлена"}
        )
