import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kewayy_project.settings')

import django
django.setup()
from kewayy_app.models import Story, TestCase


def add_story(name: str, description: str = 'Sample description', reference_url: str = None) -> Story:
    story = Story.objects.get_or_create(name=name)[0]
    story.description = description
    story.reference_url = reference_url
    story.save()
    return story


def add_test_case(story: Story, criteria: str, has_passed: bool = None, is_automated: bool = False) -> TestCase:
    test_case = TestCase.objects.get_or_create(story=story, criteria=criteria)[0]
    test_case.has_passed = has_passed
    test_case.is_automated = is_automated
    test_case.save()
    return test_case


def populate():
    test_cases_351 = [
        {
            'criteria': 'This test case has not been tested',
            'has_passed': None,
            'is_automated': False
        },
        {
            'criteria': 'This test case has passed',
            'has_passed': True,
            'is_automated': False
        },
        {
            'criteria': 'This test case has failed and is automated',
            'has_passed': False,
            'is_automated': True
        }
    ]

    stories = [
        {
            'name': 'Story-123',
            'description': 'The most basic story ever.',
            'reference_url': 'http://www.google.com',
            'test_cases': test_cases_351
        },
        {
            'name': 'Story-351',
            'description': 'The best description created by man.',
            'reference_url': 'http://www.aaronbuckles.com',
            'test_cases': []
        }
    ]

    for story in stories:
        s = add_story(story['name'], story['description'], story['reference_url'])
        for test_case in story['test_cases']:
            tc = add_test_case(s, test_case['criteria'], test_case['has_passed'], test_case['is_automated'])
    
    for s in Story.objects.all():
        for tc in TestCase.objects.filter(story=s):
            print(f'Added {tc} to {s}')


if __name__ == '__main__':
    print('Starting kewayy population script...')
    populate()