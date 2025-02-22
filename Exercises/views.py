from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

#Function-based view
def simple_message_view(request):
    return HttpResponse("Hello, this is a message from a function-based view!")

#Class-based view
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Hello, this is a message from a class-based view!"
        return context
    
#Function-based view with parameters
def greet_view(request, name):
    return HttpResponse(f"Hello, {name}! Welcome to our site.")

def dynamic_content_view(request):
    context = {
        'title': 'Dynamic Content',
        'item' :['item1', 'item2', 'item3'],
    }

    return render(request, 'dynamic_content.html', context)