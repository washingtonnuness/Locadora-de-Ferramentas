from django import forms
from django.forms import inlineformset_factory
from .models import Produtos, Categoria, Marca, Patrimonio


class ProdutctForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Produtos
        fields = '__all__'
        exclude = ('created_user', 'delete_user',
                   'create_at', 'update_at', 'delete_at')


class CategoriatForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CategoriatForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})
            field.widget.attrs['class'] = 'form-control'
        #self.fields['checkbox'].widget.attrs['class'] = 'form-check-input'


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MarcaForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})
            field.widget.attrs['class'] = 'form-control'
        self.fields['checkbox'].widget.attrs['class'] = 'form-check-input'


class PatrimonioForm(forms.ModelForm):
    class Meta:
        model = Patrimonio
        fields = ['patrimonio', ]

    def __init__(self, *args, **kwargs):
        super(PatrimonioForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


ProdutoFormset = inlineformset_factory(
    Produtos,
    Patrimonio,
    form=PatrimonioForm,
    extra=0,
    can_delete=False,
    min_num=1,
    validate_min=True,
)
