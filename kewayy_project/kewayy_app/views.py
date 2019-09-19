from django.shortcuts import render, redirect
from django.urls import reverse
from kewayy_app.models import Story, TestCase
from kewayy_app.forms import CreateTestCaseForm


def index(request):
    context = {}
    context['name'] = 'Aaron'
    return render(request, 'kewayy_app/index.html', context)


def show_story(request, story_slug):
    context = {}

    # Try to show the Story, except Story.DoesNotExist
    # context['story_slug'] = story_slug
    story = Story.objects.get(slug=story_slug)
    context['story'] = story
    context['test_cases'] = TestCase.objects.filter(story=story)
    context['create_tc_form'] = CreateTestCaseForm()

    return render(request, 'kewayy_app/show_story.html', context)


def show_all_stories(request):
    context = {}

    # Get all the stories

    return render(request, 'kewayy_app/show_all_stories.html', context)


def create_test_case(request, story_slug):
    try:
        story = Story.objects.get(slug=story_slug)
    except Story.DoesNotExist:
        story = None

    if request.method == 'POST':
        form = CreateTestCaseForm(request.POST)

        if form.is_valid():
            test_case = form.save(commit=False)
            test_case.story = story  # Assign the story it is part of
            test_case.save()
            print(f'{story} - {test_case.criteria}')
            return redirect(reverse('kewayy_app:show_story', kwargs={'story_slug': story_slug}))
        else:
            print(form.errors)

    # The form doesn't exist on this page (Only for POST, not GET)
    return redirect(reverse('kewayy_app:show_story', kwargs={'story_slug': story_slug}))


def create_story(request):
    pass
