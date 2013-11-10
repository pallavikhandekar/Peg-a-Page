from django.shortcuts import render
# Create your views here.
def load(request):
    listx = [1,2,3,4]
    return render(request, 'CRUDPeg.html',{"listx": listx})