from django.db.models import F
from kewayy_app.models import Story, TestCase


def delete_test_case(test_case: TestCase) -> int:
    """
    Deletes the test case.
    Returns the position of the test case below it OR 0
    """
    test_case.delete()

    # Update the positions of subsequent test cases
    succeeding_test_cases = TestCase.objects.filter(story=test_case.story).filter(position__gt=test_case.position)
    for tc in succeeding_test_cases:
        tc.position = F('position') - 1
        tc.save()
    
    # Return position
    return test_case.position - 1 if test_case.position > 0 else 0


def insert_test_case(test_case: TestCase) -> int:
    pass


def swap_test_case_positions(test_case: TestCase, direction: int) -> int:
    """
    Direction: 1 (Down) or -1 (Up).
    Returns the position of test_case
    """
    other_tc_position = test_case.position + direction
    if 0 <= other_tc_position < test_case.story.number_of_test_cases:
        # Swap is within bounds
        other_tc = TestCase.objects.filter(story=test_case.story).filter(position=other_tc_position)[0]
        other_tc.position = test_case.position
        test_case.position = other_tc_position

        test_case.save()
        other_tc.save()
        return other_tc_position
    else:
        return 0