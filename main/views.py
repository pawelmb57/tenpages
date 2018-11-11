from django.views.generic import TemplateView
from django.shortcuts import redirect


class IndexPageView(TemplateView):
    template_name = 'main/index.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:log_in')

        return super().dispatch(request, *args, **kwargs)

class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'
