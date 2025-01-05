from django.db import models
from config.settings import AUTH_USER_MODEL as User


class Course(models.Model):
    title = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    preview = models.ImageField(
        upload_to="education/course/previews",
        blank=True,
        null=True,
        verbose_name="Превью изображение курса",
        help_text="Загрузите превью изображение курса.",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание курса",
        help_text="Введите описание курса.",
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Автор",
        help_text="Укажите автора курса",
    )

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание урока",
        help_text="Введите описание урока.",
    )
    preview = models.ImageField(
        upload_to="education/lesson/previews",
        blank=True,
        null=True,
        verbose_name="Превью изображение урока",
        help_text="Загрузите превью изображение урока.",
    )
    link = models.TextField(
        blank=True,
        null=True,
        verbose_name="Ссылка на видео",
        help_text="Введите ссылку на видео.",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        help_text="Выберете курс",
        null=True,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Автор',
        help_text='Укажите автора урока',
    )

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
