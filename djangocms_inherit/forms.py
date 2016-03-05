# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.forms.models import ModelForm
from django.utils.translation import ugettext_lazy as _

from cms.models import Page

from .models import InheritPagePlaceholder

try:
    from django.forms.utils import ErrorList
except ImportError:
    # Django<1.7 (deprecated in Django 1.8, removed in 1.9)
    from django.forms.util import ErrorList




class InheritForm(ModelForm):

    class Meta:
        model = InheritPagePlaceholder
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')

    def for_site(self, site):
        # override the page_link fields queryset to constrain just pages for
        # current site
        self.fields['from_page'].queryset = Page.objects.drafts().on_site(site)

    def clean(self):
        cleaned_data = super(InheritForm, self).clean()
        if not cleaned_data['from_page'] and not cleaned_data['from_language']:
            self._errors['from_page'] = ErrorList(
                [_('Language or Page must be filled out')])

        return cleaned_data
