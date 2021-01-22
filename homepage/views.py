from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_statement'] = "Nice to see you!"
        context['statement_two'] = "Have you had a nice day?"
        context['third'] = "Chelsea need a win..."
        context['fourth'] = "Chelsea have had too many..."
        return context

    def say_bye(self):
        return 'Goodbye!'