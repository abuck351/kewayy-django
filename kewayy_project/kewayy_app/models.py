from django.db import models
from django.utils.text import slugify


class Story(models.Model):
    name_max_length = 32
    description_max_length = 128
    reference_url_max_length = 128

    name = models.CharField(max_length=name_max_length, unique=True)
    description = models.CharField(max_length=description_max_length, null=True)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reference_url = models.URLField(max_length=reference_url_max_length, null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Stories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def number_of_test_cases(self):
        return TestCase.objects.filter(story=self).count()

    @property
    def last_test_case_index(self):
        return self.number_of_test_cases - 1
        
    def __str__(self):
        return self.name


class TestCase(models.Model):
    criteria_max_length = 512  # Isn't enforced in the database
    notes_max_length = 256  # Isn't enforced in the database
    status_choices = (
        (None, 'Not tested'),
        (True, 'Passed'),
        (False, 'Failed')
    )
    
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    position = models.IntegerField(default=0)

    status = models.NullBooleanField(null=True, blank=True, choices=status_choices)
    is_automated = models.BooleanField(default=False)

    criteria = models.TextField(max_length=criteria_max_length)
    # tags
    # notes = models.TextField(max_length=notes_max_length)

    def save(self, *args, **kwargs):
        if not self.pk:
            # Only set position when CREATING a TestCase
            self.position = TestCase.objects.filter(story=self.story).count()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.criteria