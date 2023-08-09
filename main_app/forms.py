from django import forms
from .models import Finch


def create_bootstrap_form(**kwargs) -> forms.ModelForm:
    """Factory function to create a Bootstrap-styled ModelForm class. Uses Tempus Dominus for date fields

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
            for field_name, field in self.fields.items():
                if isinstance(field.widget, forms.widgets.DateInput):
                    field.widget.attrs.update({
                        'class': 'form-control datetimepicker-input',
                        'data-target': '#' + field_name,
                        'data-toggle': 'datetimepicker',
                    })
                elif isinstance(field.widget, forms.widgets.Select):
                    field.widget.attrs['class'] = 'form-control form-select'
                else:
                    field.widget.attrs['class'] = 'form-control'
    return BootstrapModelForm
