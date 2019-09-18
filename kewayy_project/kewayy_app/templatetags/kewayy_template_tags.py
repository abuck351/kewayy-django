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


@register.filter(name='add_attributes')
def add_attributes(field, attributes):
    """
    Add attributes to fields (from form.visible_fields, etc...)
    Attributes without a ':' are automatically assigned to be a class
    Attributes can have a ':' to specify the attibute (e.g. class:myclass)
    Example: {{ field|add_attributes:"my-awesome-class" }}
    """
    attrs = {}
    raw_attrs = attributes.split(',')

    for raw_attr in raw_attrs:
        if ':' in raw_attr:
            # attr:value
            attr, value = raw_attr.split(':')
            attrs[attr] = value
        else:
            # class:value
            attrs['class'] = raw_attr

    return field.as_widget(attrs=attrs)


@register.inclusion_tag('kewayy_app/field.html')
def display_field(field):
    return {'field': field}