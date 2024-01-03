from django import forms
from blog.models import Blog
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'preview', 'published']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'
