from django import forms

from Product.models import Product, Version

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('owner',)

        # fields = ('name', 'description', 'image', 'category', 'price',)
        fields = ['name', 'description', 'image', 'category', 'price', 'is_published']
        # fields = '__all__'
        # exclude = ['price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        # for field_name, field in self.fields.items():
        #     field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        name = self.cleaned_data['name']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in name.lower():
                raise forms.ValidationError("Название содержит запрещенные слова")
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in description.lower():
                raise forms.ValidationError("Описание содержит запрещенные слова")
        return description


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version

        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'


class ModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['description', 'category', 'is_published']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
