from django import forms
from django.forms import inlineformset_factory

from .models import Orcamento, OrcamentoItens


class OrcamentoForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Orcamento
        fields = ('cliente',)

    def __init__(self, *args, **kwargs):
        super(OrcamentoForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})
            field.widget.attrs['class'] = 'form-control'

        self.fields['cliente'].disabled = True


class OrcamentoItensForm(forms.ModelForm):
    id = forms.IntegerField()

    class Meta:
        model = OrcamentoItens
        fields = (
            'orcamento',
            'id',
            'produto',
            'patrimonio',
            'valor',
            'periodo',
        )

    def __init__(self, *args, **kwargs):
        super(OrcamentoItensForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['orcamento'].label = ''
        self.fields['orcamento'].widget = forms.HiddenInput()

        self.fields['id'].label = ''
        self.fields['id'].widget = forms.HiddenInput()


OrcamentoItemsFormset = inlineformset_factory(
    Orcamento,
    OrcamentoItens,
    form=OrcamentoItensForm,
    extra=0,
    can_delete=False,
    min_num=1,
    validate_min=True,
)
