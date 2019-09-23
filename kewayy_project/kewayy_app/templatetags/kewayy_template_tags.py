from django import template
from kewayy_app.models import Story

register = template.Library()


@register.inclusion_tag('kewayy_app/stories_sidebar.html')
def show_story_sidebar(current_story=None):
    all_stories = Story.objects.all()
    return {'current_story': current_story, 'all_stories': all_stories}


@register.inclusion_tag('kewayy_app/test_case.html')
def show_test_case(test_case, index: int):
    return {'test_case': test_case, 'index': index}


@register.inclusion_tag('kewayy_app/select.html')
def render_select(form_field):
    return {'form_field': form_field}