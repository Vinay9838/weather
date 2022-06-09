from django import forms
from django_select2.forms import HeavySelect2Widget, Select2Widget, ModelSelect2Widget, ModelSelect2MultipleWidget
from .models import City


class CityForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=City.objects.filter(status=1),
                                               required=True,
                                               widget=ModelSelect2Widget(
                                                   model=City,
                                                   search_fields=[
                                                       'name__icontains'
                                                   ]),label='Select City',)

    class Meta:
        model = City
        fields = ('name',)