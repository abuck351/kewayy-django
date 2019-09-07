from django.db import models
from django.utils.text import slugify


class Story(models.Model):
    name_max_length = 128
    reference_url_max_length = 128

    name = models.CharField(max_length=name_max_length, unique=True)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reference_url = models.URLField(max_length=reference_url_max_length, null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Stories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class TestCase(models.Model):
    criteria_max_length = 512  # Isn't enforced in the database
    notes_max_length = 256  # Isn't enforced in the database
    
    story = models.ForeignKey(Story, on_delete=models.CASCADE)

    has_passed = models.BooleanField(default=False)
    is_enabled = models.BooleanField(default=True)
    is_automated = models.BooleanField(default=False)

    criteria = models.TextField(max_length=criteria_max_length)
    # tags
    # notes = models.TextField(max_length=notes_max_length)

    def __str__(self):
        return self.criteria