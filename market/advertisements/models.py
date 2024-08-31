from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


class Advertisement(models.Model):
    image = models.ImageField(verbose_name='Image', upload_to='advertisements/', null=True, blank=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=2000, null=True, blank=True)

    CATEGORY_CHOICES = (
        ('tech', 'Техника'),
        ('cars', 'Машины'),
        ('sport', 'Спортивное'),
        ('homes', 'Недвижимость'),
        ('other', 'Другое')
    )

    STATUS_CHOICES = (
        ('moderation', 'На модерации'),
        ('accepted', 'Опубликовано'),
        ('rejected', 'Отклонено'),
        ('deleted', 'На удаление')
    )

    category = models.CharField(verbose_name='Категория', max_length=50, choices=CATEGORY_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(verbose_name='Статус', max_length=50, choices=STATUS_CHOICES)

    is_active = models.BooleanField(default=True)

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    publicate_time = models.DateTimeField(null=True, blank=True)
