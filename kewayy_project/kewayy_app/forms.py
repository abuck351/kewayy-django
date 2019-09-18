from django import forms
from kewayy_app.models import TestCase


class CreateTestCaseForm(forms.ModelForm):
    is_enabled = forms.BooleanField(required=False)
    is_automated = forms.BooleanField(required=False)
    criteria = forms.CharField(
        widget=forms.Textarea,
        max_length=TestCase.criteria_max_length, 
        help_text='Please write the criteria for the test case.')

    class Meta:
        model = TestCase
        exclude = ('story', 'has_passed')