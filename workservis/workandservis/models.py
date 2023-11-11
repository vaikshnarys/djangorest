from django.contrib.auth.models import User
from django.db import models

class Workservis(models.Model):
    ACTIVE = "ACTIVE"
    DRAFT = "DRAFT"
    ARCHIVE = "ARCHIVE"

    KIND_CHOICES = [
        (ACTIVE, "Active"),
        (DRAFT, "Draft"),
        (ARCHIVE, "Archive"),
    ]
    kind = models.CharField(max_length=10, choices=KIND_CHOICES, default=DRAFT)
    title = models.CharField(max_length=200, null = False)
    description = models.TextField(blank=True)
    price = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null = True)
    user = models.ForeignKey(User,verbose_name='User', on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

class Comments(models.Model):
    working_servis = models.ForeignKey(Workservis,null = True, on_delete=models.CASCADE,related_name='comments')
    text = models.TextField(max_length=200)