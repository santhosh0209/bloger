from django.db import models
from django.utils import timezone



EVENT_STATUSES = (
    (0, 'none'),
    (1, 'love'),
    (2, 'family'),
    (3, 'self love'),
    (4, 'he nd she'),
    (5, 'frames of love')
)
EVENT_STATUSES2 = (
    (0, 'none'),
    (1, 'love'),
    (2, 'family'),
    (3, 'self love'),
    (4, 'he nd she'),
    (5, 'frames of love')
)

class Post(models.Model):
    no = models.IntegerField(default=None)
    image = models.ImageField(upload_to='images', blank=False, default=None)
    category = models.CharField(max_length=200, default=None)
    category_filter = models.PositiveIntegerField(
    choices=EVENT_STATUSES,
    default='0',
    )

    category_filter2 = models.PositiveIntegerField(
    choices=EVENT_STATUSES2,
    default='0',
    )