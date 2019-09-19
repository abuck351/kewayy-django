from django import forms
from kewayy_app.models import TestCase


class CreateTestCaseForm(forms.ModelForm):
    is_automated = forms.BooleanField(
        required=False,
        label="Automated?"
    )
    criteria = forms.CharField(
        widget=forms.Textarea, 
        help_text='Please write the criteria for the test case.'
    )

    class Meta:
        model = TestCase
        exclude = ('story', 'has_passed')