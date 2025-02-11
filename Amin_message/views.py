from django.views.generic import TemplateView

class MessageView(TemplateView):
    template_name = 'home.html'

