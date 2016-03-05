# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cms.models.fields import PageField
from cms.utils.i18n import get_language_tuple


@python_2_unicode_compatible
class InheritPagePlaceholder(CMSPlugin):
    """
    Provides the ability to inherit plugins for a certain placeholder from an
    associated 'parent' page instance
    """
    from_page = PageField(
        null=True,
        help_text=_('Choose a page to include its plugins into this '
                    'placeholder, empty will choose current page'))

    from_language = models.CharField(
        _('language'), max_length=5, choices=get_language_tuple(), blank=True,
        null=True, help_text=_('Optional: the language of the plugins you want'))

    def __str__(self):
        desc = ''
        if self.from_language:
            if self.from_page:
                desc += _(' page {0} -').format(self.from_page.get_title(self.from_language))
                desc += _(' language {0}').format(self.from_language)
        elif self.from_page:
            desc += _(' page {0}').format(self.from_page.get_title(self.language))
        return _('Inherit content from{0}').format(desc)
