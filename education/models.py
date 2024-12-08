from django.db import models


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

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
