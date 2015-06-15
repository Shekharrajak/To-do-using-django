from django.shortcuts import render_to_response
from models import todo

# Create your views here.

def index(request):

	item =todo.objects.all()

	return render_to_response('index.html',{'item':items})