from django.forms import ModelForm
from .models import Orcamentos
from backend.produtos.models import Produtos


class OrcamentosForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Orcamentos
        fields = '__all__'
        exclude = ('cliente', 'created_user', 'delete_user',
                   'create_at', 'update_at', 'delete_at')

    def __init__(self, *args, **kwargs):
        super(OrcamentosForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})
            field.widget.attrs['class'] = 'form-control'
