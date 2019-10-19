from django import forms
from kewayy_app.models import Story, TestCase


class CreateTestCaseForm(forms.ModelForm):
    is_automated = forms.BooleanField(required=False, label='Automated?')
    criteria = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}), help_text='Please write the criteria for the test case.')

    class Meta:
        model = TestCase
        exclude = ('story', 'status', 'position')


class EditTestCaseForm(forms.ModelForm):
    story = forms.ModelChoiceField(queryset=Story.objects.all(), label="Story")
    status = forms.NullBooleanField(required=False, widget=forms.Select(choices=TestCase.status_choices), label='Test Case Status')
    is_automated = forms.BooleanField(required=False, label='Automated?')
    criteria = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}), help_text='Please write the criteria for the test case.')

    class Meta:
        model = TestCase
        fields = ('story', 'status', 'is_automated', 'criteria')


class CreateStoryForm(forms.ModelForm):

    class Meta:
        model = Story
        exclude = ('slug',)

class EditStoryForm(forms.ModelForm):
    
    class Meta:
        model = Story
        exclude = ('slug',)
