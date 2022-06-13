from django import forms
from .models import Contact


class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = Contact
        # fields = ['article', 'name', 'image', 'email', 'website', 'message']
        fields = '__all__'
        exclude = ('author', 'article')

    def __init__(self, *args, **kwargs):
        super(ContactCreateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
