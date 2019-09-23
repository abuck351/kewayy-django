from django.shortcuts import render, redirect
from django.urls import reverse
from kewayy_app.models import Story, TestCase
from kewayy_app.forms import CreateTestCaseForm, EditTestCaseForm
import kewayy_app.forms as kewayy_forms


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
    context['test_cases'] = TestCase.objects.filter(story=story).order_by('position')
    context['create_tc_form'] = kewayy_forms.CreateTestCaseForm()

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
        form = kewayy_forms.CreateTestCaseForm(request.POST)

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


def edit_test_case(request, test_case_id: int):
    try:
        test_case = TestCase.objects.get(pk=test_case_id)
    except TestCase.DoesNotExist:
        # Go back to the home page if the Test Case doesn't exist
        return redirect(reverse('kewayy_app:index'))

    form = kewayy_forms.EditTestCaseForm(request.POST or None, instance=test_case)

    # POST
    if request.method == 'POST':
        if form.is_valid():
            saved_test_case = form.save()
            print(f'Updated Test Case {saved_test_case.pk}')
            page_position = f'#testcase{test_case.position}'
            return redirect(reverse('kewayy_app:show_story', kwargs={'story_slug': saved_test_case.story.slug}) + page_position)
        else:
            print(form.errors)
    
    # GET
    context = {}
    context['test_case'] = test_case
    context['form'] = form
    return render(request, 'kewayy_app/edit_test_case.html', context)


def create_story(request):
    pass
