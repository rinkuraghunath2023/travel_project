from django.shortcuts import render
from.models import tour,people

# Create your views here.
def index(request):
    obj=tour.objects.all()
    ppl = people.objects.all()
    return render(request, 'index.html',{'result': obj,'result1': ppl})
