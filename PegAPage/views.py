from django.shortcuts import render,render_to_response,RequestContext,HttpResponseRedirect
from PegAPage.models import *
from PegAPage.forms import *
from django.http.response import HttpResponse

# Create your views here.
def load(request):
    listx = [1,2,3,4]
    return render(request, 'CRUD_Peg.html',{"listx": listx})

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
    if request.method == 'POST':
        print  request.POST['bid']
        board = Board.objects.get(id=request.POST['bid'])
        pegs =board.peg_set.all()    
    #return render(request,'Pegs.html',{'pegs':pegs,'boardid':board.id})
    return HttpResponse("Test")

def loadUI(request):
    board = Board.objects.get(id=1)
    pegs =board.peg_set.all()
    listofPegs = [peg for peg in pegs]    
    return render(request,'Boards.html',{'pegs':listofPegs,'boardid':board.id})
    #return HttpResponse("Test")
    
def deletePeg(request):
    if request.method == 'POST':
        board = Board.objects.get(id=request.POST['boardid'])
        peg = Peg.objects.get(id= request.POST['pegid'])
        board.peg_set.remove(peg)
        board.save()
        peg.delete()
        print "delete"
        return HttpResponse("Peg Deleted")
    else:
        form = PegCreateForm()
        variables = RequestContext(request, {'form': form})
        return render_to_response('CRUD_Peg.html', variables)
   
    
def updatePeg(request):
    url = request.POST['url']
    name = request.POST['name']
    desc = request.POST['desc']
    peg = Peg.objects.get(id= request.POST['pegid'])
    peg.url = url
    peg.name = name
    peg.peg_des = desc
    peg.save()
    print desc
    print "update"
    return HttpResponse("Peg Updated")

def commentPeg(request):
    #if request.method == 'POST':
    if request.method == 'POST':
        form = CommentPegForm(request.POST)
        #board = Board.objects.get(id=request.POST['boardid'])
        #peg = Peg.objects.get(id= request.POST['pegid'])
        #user = User.objects.get(id= request.POST['userid'])
        comment, dummy = Comments.objects.get_or_create(
                comments_desc = request.POST['commentdesc'],
                user_id = request.POST['userid'],
                board_id = request.POST['boardid'],
                peg_id = request.POST['pegid']
                )
        comment.save()
        return HttpResponse("Comment Saved")
    else:    
        form = CommentPegForm(request.POST)
        variables = RequestContext(request, {'form': form})
        return render_to_response('Comment_Peg.html', variables)
    
#################### END PEG METHODS ##################

#Board methods#
#Board methods#
def create_board(request):
    if request.method == 'POST':
        form = BoardCreateForm(request.POST)
        if form.is_valid():
            print "VALID"
            # Create Board
            board, dummy = Board.objects.get_or_create(
                Board_name = form.cleaned_data['name'],
                user_id = "1",                
                Board_des = form.cleaned_data['desc']
            )
            Board.save(board)
            #mmboard= Board.objects.get(id = 1)
           
            #mmboard.save()
                #boardname = request.POST['boardname']            
         
            return HttpResponse("Board Saved")
        else:
            print "INVALID"
            form = BoardCreateForm()
            variables = RequestContext(request, {'form': form})
            return render_to_response('CRUD_Board.html', variables)   
    else:
        print "VALID Load"
        form = BoardCreateForm()
        variables = RequestContext(request, {'form': form})
        return render_to_response('CRUD_Board.html', variables)
    
def loadBoard(request):
    boards = Board.objects.all().filter(user = 1)     
   
    listofBoards = [b for b in boards] 
    return render(request,'Boards.html',{'boards':listofBoards})
    #return HttpResponse("Test")
    
def deleteBoard(request):
    if request.method == 'POST':
        board = Board.objects.get(id=request.POST['bid'])       
        board.delete()    
        print "delete"
        return HttpResponse("Board Deleted")
    else:
        form = BoardCreateForm()
        variables = RequestContext(request, {'form': form})
        return render_to_response('CRUD_Board.html', variables)

def updateBoard(request):   
    name = request.POST['name']
    desc = request.POST['desc']
    board = Board.objects.get(id= request.POST['bid'])   
    board.Board_name = name
    board.Board_des = desc
    board.save()
    print desc
    print "update"
    return HttpResponse("Board Updated")
 
def pegitPeg(request):
    if request.method == 'POST':
        form = PegItForm(request.POST)
        if form.is_valid():
            print "VALID"
            # Create Peg
            peg, dummy = Peg.objects.get_or_create(
                url = request.POST['url'],         #form.cleaned_data['url'],
                name = request.POST['name'], #form.cleaned_data['name'],
                peg_des = request.POST['desc'], #form.cleaned_data['desc']
                boards = request.POST['bname']
            )
            myboard = Board.objects.get(id = 1)
            #boardname = request.POST['boardname']
            myboard.peg_set.add(peg)
            myboard.save()
            return HttpResponse("RePegged")
        else:
            print "INVALID"
            form = PegItForm()
            variables = RequestContext(request, {'form': form})
            return render_to_response('PegIt.html', variables)
    else:
        print "VALID LOad"
        form = PegItForm()
        variables = RequestContext(request, {'form': form})
        return render_to_response('PegIt.html', variables)