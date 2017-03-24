from django.views.generic import TemplateView


home = TemplateView.as_view(
    template_name='frontend/index.html'
)


accounts_receivable = TemplateView.as_view(
    template_name='frontend/accounts_receivable.html'
)
