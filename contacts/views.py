# Create your views here.

from django.shortcuts import render_to_response

def list(request):
    return render_to_response('contacts/list.html', {'greeting': 'hello'})
