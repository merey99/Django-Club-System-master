from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from django import forms

from elearn.models import (Learner, Instructor, Course, User, Announcement, Tutorial)

from django.db import connection

class PostForm(forms.ModelForm):

    interests = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        required=True,
        widget=forms.CheckboxSelectMultiple
    )

    meeting = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'format': '%Y-%m-%dT%H:%M'}),
        required=False
    )

    class Meta:
        model = Announcement
        fields = ('content', 'meeting', 'interests')



class ProfileForm(forms.ModelForm):
    email=forms.EmailField(widget=forms.EmailInput())
    confirm_email=forms.EmailField(widget=forms.EmailInput())

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',

        ]

    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")

        if email != confirm_email:
            raise forms.ValidationError(
                "Emails must match!"
            )



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class InstructorSignUpForm(UserCreationForm):
    interests = forms.ModelMultipleChoiceField(
        queryset = Course.objects.all(), required = True
    )

    class Meta(UserCreationForm.Meta):
        model = User


    def __init__(self, *args, **kwargs):
            super(InstructorSignUpForm, self).__init__(*args, **kwargs)

            for fieldname in ['username', 'password1', 'password2']:
                self.fields[fieldname].help_text = None

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_instructor = True
        if commit:
            user.save()
            instructor = Instructor.objects.create(user=user)
            instructor.interest.add(*self.cleaned_data.get('interests'))
        return user



class LearnerSignUpForm(UserCreationForm):
    interests = forms.ModelMultipleChoiceField(
        queryset = Course.objects.all(), required = True
    )

    class Meta(UserCreationForm.Meta):
        model = User


    def __init__(self, *args, **kwargs):
            super(LearnerSignUpForm, self).__init__(*args, **kwargs)

            for fieldname in ['username', 'password1', 'password2']:
                self.fields[fieldname].help_text = None

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_learner = True
        user.save()
        learner = Learner.objects.create(user=user)
        learner.interests.add(*self.cleaned_data.get('interests'))
        return user



class LearnerInterestsForm(forms.ModelForm):
    class Meta:
        model = Learner
        fields = ('interests', )
        widgets = {
            'interests': forms.CheckboxSelectMultiple
        }


class BaseAnswerInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()

        has_one_correct_answer = False
        for form in self.forms:
            if not form.cleaned_data.get('DELETE', False):
                if form.cleaned_data.get('is_correct', False):
                    has_one_correct_answer = True
                    break
        if not has_one_correct_answer:
            raise ValidationError('Mark at least one answer as correct.', code='no_correct_answer')

class LearnerCourse(forms.ModelForm):
    class Meta:
        model = Learner
        fields = ('interests', )
        widgets = {
            'interests': forms.CheckboxSelectMultiple
        }

    @transaction.atomic
    def save(self):
        learner = Learner()
        learner.interests.add(*self.cleaned_data.get('interests'))
        return learner_id

