from django import template
from kewayy_app.models import Story

register = template.Library()


@register.inclusion_tag('kewayy_app/stories_sidebar.html')
def show_story_sidebar(current_story=None):
    all_stories = Story.objects.all()

    return {'current_story': current_story, 'all_stories': all_stories}