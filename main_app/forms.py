from django import forms
from .models import Finch


def create_bootstrap_form(**kwargs):
    """Factory function to create a Bootstrap-styled ModelForm class.
    
    Args:
        Keyword args:
        *  model (``django.db.models.Model``): required argument -- Model class for the form
        *  fields (``List | String``): required argument --  The fields to be included in the form, either a list of field names or '__all__'


    Returns:
        ``BootstrapModelForm``: An object inheriting from ``django.forms.ModelForm`` that has Bootstrap `form-control` class applied to its widgets
    """
    class BootstrapModelForm(forms.ModelForm):
        class Meta:
            model = kwargs['model']
            fields = kwargs['fields']

        # Add `form-control` class to all fields' widgets without explicitly doing it for each field.
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'
    return BootstrapModelForm
