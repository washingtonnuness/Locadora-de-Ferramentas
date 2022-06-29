from django.forms import ModelForm, inlineformset_factory

from backend.produtos.models import Produtos

from .models import Orcamentos, OrcamentosItens


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


class OrcamentosItensForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = OrcamentosItens
        fields = '__all__'
        exclude = ('cliente', 'created_user', 'delete_user',
                   'create_at', 'update_at', 'delete_at')

    def __init__(self, *args, **kwargs):
        super(OrcamentosItens, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})
            field.widget.attrs['class'] = 'form-control'


OrcamentosFormSet = inlineformset_factory(
    Orcamentos,
    OrcamentosItens,
    form=OrcamentosItensForm,
    extra=0,
    can_delete=False,
    min_num=1,
    validate_min=True,
)
