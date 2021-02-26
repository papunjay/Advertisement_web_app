from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.
crew_choices=(
    ('solo','solo'),
    ('small','small'),
    ('large','large'),
)

category_choices=(
    ('code','code'),
    ('mobile_review','mobile_review'),
    ('vlogs','vlogs'),
    ('comedy','comedy'),
    ('Gaming','Gaming'),
    ('film_making','film_making'),
    ('cooking','coocking'),
)

camera_choices=(
    ('nikon','nikon'),
    ('red','red'),
    ('fuji','fuji'),
    ('panasonic','panasonic'),
    ('other','other'),
)

class Youtuber(models.Model):
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    photo=models.ImageField(upload_to='media/youtuber/%Y/%m')
    video_url=models.CharField(max_length=255)
    description=RichTextField()
    city=models.CharField(max_length=255)
    age=models.IntegerField()
    height=models.IntegerField()
    crew=models.CharField(choices=crew_choices,max_length=255)
    camera_type=models.CharField(choices=camera_choices,max_length=255)
    sub_count=models.CharField(max_length=255)
    category=models.CharField(choices=category_choices,max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date=models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.name
        