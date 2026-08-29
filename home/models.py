from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Product(models.Model):

    CATEGORY_CHOICES = [
        ("waterproofing", "Waterproofing"),
        ("flooring", "Flooring"),
        ("road-surfacing", "Road Surfacing"),
        ("restofix", "Restofix"),
    ]

    name = models.CharField(max_length=200)

    subtitle = models.CharField(
        max_length=300,
        blank=True
    )

    description = CKEditor5Field(
        "Description",
        config_name="extends",
        blank=True
    )

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES
    )

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    tds_file = models.FileField(
        upload_to="products/tds/",
        blank=True,
        null=True
    )

    msds_file = models.FileField(
        upload_to="products/msds/",
        blank=True,
        null=True
    )

    featured = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name

from django.utils.text import slugify
class ProductCategory(models.Model):

 

    name = models.CharField(max_length=200)

    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True
    )

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

   
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name