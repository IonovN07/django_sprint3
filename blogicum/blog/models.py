from core.models import BasePublishedModel
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Category(BasePublishedModel):
    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    

class Location(BasePublishedModel):
    name = models.CharField(max_length=256)
    
    
class Post(BasePublishedModel):
    title = models.CharField(max_length=256)
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts_author'           
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts_by_location'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts_in_category'
    )
    