from django.shortcuts import render
from kewayy_app.models import Story, TestCase


def index(request):
    context = {}
    context['name'] = 'Aaron'
    return render(request, 'kewayy_app/index.html', context)


def show_story(request, story_slug):
    context = {}

    # Try to show the Story, except Story.DoesNotExist
    # context['story_slug'] = story_slug
    context['story'] = Story.objects.get(slug=story_slug)

    return render(request, 'kewayy_app/show_story.html', context)


def show_all_stories(request):
    context = {}

    # Get all the stories

    return render(request, 'kewayy_app/show_all_stories.html', context)


def create_story(request):
    pass
