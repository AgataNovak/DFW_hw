import re

from rest_framework.serializers import ValidationError


class LinkValidator:
    """Валидатор проверяет, что, указанная при сохранении урока или курса, ссылка ведет на youtube"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        field = dict(value).get(self.field)
        if field:
            reg_link = re.compile(r'https:\S+')
            reg_youtube = re.compile('youtube.com')
            links = re.findall(reg_link, field)
            for link in links:
                if not re.match(reg_youtube, link):
                    raise ValidationError('Ссылки не могут вести на сторонние ресурсы кроме Youtube')