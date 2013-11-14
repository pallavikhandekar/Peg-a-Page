from django.shortcuts import render,render_to_response,RequestContext,HttpResponseRedirect
from PegAPage.models import *
from PegAPage.forms import *
from django.http.response import HttpResponse

# Create your views here.
def load(request):
    listx = [1,2,3,4]
    return render(request, 'CRUDPeg.html',{"listx": listx})

####################PEG METHODS ##################

def create_peg(request):
    if request.method == 'POST':
        form = PegCreateForm(request.POST)
        if form.is_valid():
            print "VALID"
            # Create Peg
            peg, dummy = Peg.objects.get_or_create(
                url = form.cleaned_data['url'],
                name = form.cleaned_data['name'],
                peg_des = form.cleaned_data['desc']
            )
            myboard = Board.objects.get(id = 1)
            #boardname = request.POST['boardname']
            myboard.peg_set.add(peg)
            myboard.save()
            return HttpResponse("Peg Saved")
        else:
            print "INVALID"
            form = PegCreateForm()
            variables = RequestContext(request, {'form': form})
            return render_to_response('CRUD_Peg.html', variables)
    else:
        print "VALID LOad"
        form = PegCreateForm()
        variables = RequestContext(request, {'form': form})
        return render_to_response('CRUD_Peg.html', variables)
    
def loadPeg(request):
    board = Board.objects.get(id=1)
    pegs =board.peg_set.all()
    listofPegs = [peg for peg in pegs] 
    return render(request,'Pegs.html',{'pegs':listofPegs,'boardid':board.id})
    #return HttpResponse("Test")

def deletePeg(request):
    if request.method == 'POST':
        board = Board.objects.get(id=request.POST['boardid'])
        peg = Peg.objects.get(id= request.POST['pegid'])
        board.peg_set.remove(peg)
        board.save()
        peg.delete()
        peg.save()
        print "delete"
        return HttpResponse("Peg Deleted")
    else:
        form = PegCreateForm()
        variables = RequestContext(request, {'form': form})
        return render_to_response('CRUD_Peg.html', variables)
   
    
def updatePeg(request):
    url = request.POST['url']
    title = request.POST['title']
    peg = request.POST['peg']
    form = PegCreateForm({
         'url': url,
         'title': title,
         'pegs': peg
         })
    print "update"
    
#################### END PEG METHODS ##################