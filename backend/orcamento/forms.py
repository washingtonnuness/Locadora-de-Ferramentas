from django.forms import ModelForm, inlineformset_factory

from .models import Orcamento, OrcamentoItens


class OrcamentoForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Orcamento
        fields = '__all__'
        exclude = ('cliente', 'created_user', 'delete_user',
                   'create_at', 'update_at', 'delete_at')

    def __init__(self, *args, **kwargs):
        super(OrcamentoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})
            field.widget.attrs['class'] = 'form-control'


class OrcamentoItensForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = OrcamentoItens
        fields = '__all__'
        exclude = ('cliente', 'created_user', 'delete_user',
                   'create_at', 'update_at', 'delete_at')

    def __init__(self, *args, **kwargs):
        super(OrcamentoItens, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})
            field.widget.attrs['class'] = 'form-control'


OrcamentoFormSet = inlineformset_factory(
    Orcamento,
    OrcamentoItens,
    form=OrcamentoItensForm,
    extra=0,
    can_delete=False,
    min_num=1,
    validate_min=True,
)
