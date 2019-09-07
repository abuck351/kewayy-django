from django.contrib import admin

from kewayy_app.models import Story, TestCase


class TestCaseInline(admin.TabularInline):
    model = TestCase


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [TestCaseInline]


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['story', 'criteria']
