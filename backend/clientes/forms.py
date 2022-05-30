from django import forms

from .models import Clientes


class ClientesForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Clientes
        fields = '__all__'
        exclude = ('created_user', 'delete_user',
                   'create_at', 'update_at', 'delete_at')

    def __init__(self, *args, **kwargs):
        super(ClientesForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})
            field.widget.attrs['class'] = 'form-control'
        self.fields['tipo'].widget.attrs['onchange'] = "getElement(this.value,'element')"
