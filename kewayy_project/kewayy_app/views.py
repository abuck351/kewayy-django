from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import F
from kewayy_app.models import Story, TestCase
from kewayy_app.forms import CreateTestCaseForm, EditTestCaseForm, CreateStoryForm, EditStoryForm
import kewayy_app.forms as kewayy_forms


def index(request):
    context = {}
    context['name'] = 'Aaron'
    return render(request, 'kewayy_app/index.html', context)


def show_story(request, story_slug):
    story = get_object_or_404(Story, slug=story_slug)
    edit_story_form = kewayy_forms.EditStoryForm(request.POST or None, instance=story)

    # POST
    if request.method == 'POST':
        if edit_story_form.is_valid():
            saved_story = edit_story_form.save()
            print(f'Updated Story {story_slug}')
            return redirect(reverse('kewayy_app:show_story', kwargs={'story_slug': saved_story.slug}))
        else:
            print(edit_story_form.errors)

    # GET
    context = {}
    context['story'] = story
    context['test_cases'] = TestCase.objects.filter(story=story).order_by('position')
    context['create_tc_form'] = kewayy_forms.CreateTestCaseForm()
    context['edit_story_form'] = edit_story_form

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
            print(f'Created testcase - {test_case.criteria} in {story}')
            page_position = f'#testcase{test_case.position}'
            return redirect(reverse('kewayy_app:show_story', kwargs={'story_slug': story_slug}) + page_position)
        else:
            print(form.errors)

    # The form doesn't exist on this page (Only for POST, not GET)
    return redirect(reverse('kewayy_app:show_story', kwargs={'story_slug': story_slug}))


def edit_test_case(request, test_case_id: int):
    test_case = get_object_or_404(TestCase, pk=test_case_id)
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


def change_test_case_status(request, test_case_id: int):
    tc = get_object_or_404(TestCase, pk=test_case_id)

    # POST
    if request.method == 'POST':
        print(tc.status)
        tc.status = True if tc.status is None or tc.status == False else False
        tc.save()
        print(f'Updated Test Case Status {tc.pk}')
        # Redirect below
    
    # Shouldn't be able to GET to this page (Only for POST)
    page_position = f'#testcase{tc.position}'
    return redirect(reverse('kewayy_app:show_story', kwargs={'story_slug': tc.story.slug}) + page_position)


def delete_test_case(request, test_case_id: int):
    test_case = get_object_or_404(TestCase, pk=test_case_id)
    test_case.delete()

    # Reorder all the other test cases
    succeeding_test_cases = TestCase.objects.filter(story=test_case.story).filter(position__gt=test_case.position)
    for tc in succeeding_test_cases:
        tc.position = F('position') - 1
        tc.save()

    # Redirect
    page_position = ''
    if TestCase.objects.filter(story=test_case.story).count() > 1:
        new_position = test_case.position - 1 if test_case.position > 0 else 0
        page_position = f'#testcase{new_position}'
    return redirect(reverse('kewayy_app:show_story', kwargs={'story_slug': test_case.story.slug}) + page_position)


def create_story(request):
    create_story_form = kewayy_forms.CreateStoryForm()
    
    # POST
    if request.method == 'POST':
        form = kewayy_forms.CreateStoryForm(request.POST)
        if form.is_valid():
            saved_story = form.save(commit=True)
            print(f'Created Story {saved_story.slug}')
            return redirect(reverse('kewayy_app:show_story', kwargs={'story_slug': saved_story.slug}))
        else:
            print(form.errors)
    
    # GET
    context = {}
    context['form'] = create_story_form
    return render(request, 'kewayy_app/create_story.html', context)


