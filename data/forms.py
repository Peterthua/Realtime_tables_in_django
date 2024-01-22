from .models import Profile, Post
from django.forms import ModelForm, CheckboxInput, DateInput, Select
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Div
from crispy_forms.bootstrap import StrictButton


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'status': Select(attrs={
                'class': 'form-control'
            })
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_id = 'post-form'
        # title, content, status, author
        self.helper.layout = Layout(
            Row(
                Column('title'),
                Column('status'),
                
            ),
            'content',
            'author',
            Div(
                # Submit('submit', 'Submit', css_class='btn btn-primary w-100 px-5 py-2 mt-3 '),
                StrictButton('Submit', type='submit', css_class='btn btn-outline-info w-100 px-5 py-2 mt-3'),
                css_class='text-center w-100'
            )
        )


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'receive_email_notifications': CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'birth_date': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            })

        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        # first_name, last_name, email, birth_date, location, bio, receive_email_notifications, language_preference
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_id = 'create-profile'
        self.helper.layout = Layout(
            Row(
                Column('first_name'),
                Column('last_name'),
                
            ),
            'email',
            Row(
                Column('birth_date'),
                Column('location'),
                
            ),
            'bio',
            Row(
                Column('receive_email_notifications'),
                Column('language_preference'),
                
            ),
            Div(
                # Submit('submit', 'Submit', css_class='btn btn-primary w-100 px-5 py-2 mt-3 '),
                StrictButton('Add Profile', type='submit', css_class='btn btn-outline-info w-100 px-5 py-2 mt-3'),
                css_class='text-center w-100'
            )
        )
