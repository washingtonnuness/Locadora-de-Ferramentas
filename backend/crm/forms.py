from django import forms

from .models import Cliente, Fornecedor


class ClienteForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Cliente
        fields = (
            'tipo',
            'cnpj',
            'rg',
            'cpf',
            'nome',
            'razao_social',
            'nome_fantasia',
            'address',
            'address_number',
            'complement',
            'district',
            'city',
            'uf',
            'cep',
            'endereco_entrega',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})
            field.widget.attrs['class'] = 'form-control'

        self.fields['tipo'].widget.attrs['onchange'] = "getElement(this.value,'element')"


class FornecedorForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Fornecedor
        fields = (
            'tipo',
            'cnpj',
            'rg',
            'cpf',
            'nome',
            'razao_social',
            'nome_fantasia',
            'address',
            'address_number',
            'complement',
            'district',
            'city',
            'uf',
            'cep',
            'endereco_entrega',
            'condicao_pagamento',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})
            field.widget.attrs['class'] = 'form-control'

        self.fields['tipo'].widget.attrs['onchange'] = "getElement(this.value,'element')"
