from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
# Create your views here.

class SarwarMithuRedirectView(RedirectView):
    url = 'http://www.geekyshows.com'


class MithuRedirectView(RedirectView):
    pattern_name = 'mindex'

    permanent = True      # method by default False hoye thake
    query_string = True   # method by default False hoye thake

    def get_redirect_url(self, *args, **kwargs):    # method
        return super().get_redirect_url(*args, **kwargs)