from django import forms
from . import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
import datetime
from django.utils.timezone import utc
from django.core.exceptions import ValidationError


class TalkListForm(forms.ModelForm):
    class Meta:
        fields = ('name', )
        model = models.TalkList

    def __init__(self, *args, **kwargs):
        super(TalkListForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            ButtonHolder(
                Submit('create', 'Create', css_class='btn btn-success')
            )
        )


class TalkForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'room', 'when', 'host')
        model = models.Talk

    def __init__(self, *args, **kwargs):
        super(TalkForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'room',
            'host',
            'when',
            ButtonHolder(Submit('add', 'Add', css_class='btn btn-success'))
        )

    def clean(self):
        when = self.cleaned_data.get('when')
        start = datetime.datetime(2018, 3, 30).replace(tzinfo=utc)
        end = datetime.datetime(2018, 4, 10).replace(tzinfo=utc)
        if not start < when < end:
            raise ValidationError('When is outside')
        return when