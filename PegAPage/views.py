from django.shortcuts import render,render_to_response,RequestContext,HttpResponseRedirect
from PegAPage.models import *
from PegAPage.forms import *
from PegAPage.BookmarkManager import *
from django.http.response import HttpResponse
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth import logout

  
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                                            username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password1'],
                                            email=form.cleaned_data['email']
                                            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    
    variables = RequestContext(request, {'form': form })
    return render_to_response('registration/register.html', variables )

def contactMe_page(request):
    return render(request, 'ContactMe.html')    

def privacyPolicy_page(request):
    return render(request, 'PrivacyPolicy.html')      


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
            boardid = 1# request.POST['boardid']
            savePeg(form,boardid)
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
        global_boardid=  request.POST['bid']
        request.session["boardid"] = global_boardid
    else:
        global_boardid=request.session["boardid"]
        pegs = getPegsForBoard(global_boardid)  
        liked = {}
        for peg in pegs:
            isliked = Like.objects.filter(peg_id__exact=peg.id).filter(board_id__exact=global_boardid)
            if isliked.exists():
                liked[peg.id] = "images/heart.png"
            else:
                liked[peg.id] = "images/gray_heart.png" 
      
    return render(request,'Pegs.html',{'pegs':pegs,'boardid':global_boardid, 'liked':liked})
    #return HttpResponse("Test")

def loadUI(request):
    board = Board.objects.get(id=1)
    pegs =board.peg_set.all()
    listofPegs = [peg for peg in pegs]    
    return render(request,'Boards.html',{'pegs':listofPegs,'boardid':board.id})
    #return HttpResponse("Test")
    
def deletePeg(request):
    if request.method == 'POST':
        boardid=request.POST['boardid']
        pegid = request.POST['pegid']
        removePegforBoard(boardid,pegid)
        if request.session['userid'] != getBoard(boardid).user.id:      
            removePeg() 
        return HttpResponse("Peg Deleted")
    else:
        form = PegCreateForm()
        variables = RequestContext(request, {'form': form})
        return render_to_response('CRUD_Peg.html', variables)
   
    
def editPeg(request):
    url = request.POST['url']
    name = request.POST['name']
    desc = request.POST['desc']
    pegid = request.POST['pegid']
    modifyPeg(url,name,desc,pegid)
    return HttpResponse("Peg Updated")
   
    
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
        if request.POST['ptype'] == 'comment' :
            comment, dummy = Comments.objects.get_or_create(
                    comments_desc = request.POST['commentdesc'],
                    user_id = request.POST['userid'],
                    board_id = request.POST['boardid'],
                    peg_id = request.POST['pegid']
                    )
            comment.save()
            return HttpResponse("Comment Saved")
        else:
            follow, dummy=Follow.objects.get_or_create(
            user_id = request.POST['userid'],
            board_id = request.POST['boardid']
                
                ) 
            follow.save()
            variables = RequestContext(request, {'form': form})
            return render_to_response('Comment_Peg.html', variables)
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
    #Set session user id
    request.session['userid'] = 1
    listofBoards = [b for b in boards] 
    return render(request,'Boards.html',{'boards':listofBoards})
    #return HttpResponse("Test")
    
def deleteBoard(request):
    if request.method == 'POST':
        board = Board.objects.get(id=request.POST['bid'])  
        Peg.objects.filter(boards = request.POST['bid']).delete()       
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
    userid = request.session['userid']
    error = "" 
    if request.method == 'POST':
        boardname =  request.POST['bname']
        form = PegItForm(request.POST)
        if form.is_valid():
            print "VALID"
            found_board = False
            pegid = request.POST['pegid']
            originalboardid = request.POST['boardid']
            board = Board.objects.get(id=originalboardid)
            oridinaluser_id = board.user.id
            print oridinaluser_id
            #Check Board Name:
            boardOfUser= Board.objects.filter(user_id = userid)
            for b in boardOfUser:
                if b.Board_name ==  boardname:
                    newBoard = b
                    found_board = True
                    break
                
            if found_board == False:
                    form = PegItForm()
                    variables = RequestContext(request, {'form': form,'message':"Error: Incorrect BoardName!"})
                    return render_to_response('PegIt.html', variables)
            elif boardname == board.Board_name :
                    form = PegItForm()
                    variables = RequestContext(request, {'form': form,'message':"Error: Already on Current Board"})
                    return render_to_response('PegIt.html', variables)
            else:        
                    if userid != oridinaluser_id:
                        # Create Peg
                        peg, dummy = Peg.objects.get_or_create(
                             url = request.POST['url'],         #form.cleaned_data['url'],
                             name = request.POST['name'], #form.cleaned_data['name'],
                             peg_des = request.POST['desc'], #form.cleaned_data['desc']
                            boards = request.POST['bname']
                        )
                    else:
                        peg  = Peg.objects.get(id = pegid)
                        
                    myboard = Board.objects.get(id = newBoard.id)
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
        form = PegItForm()
        variables = RequestContext(request, {'form': form,'message':""})
        return render_to_response('PegIt.html', variables)
        
def LikePeg(request):
            print "VALID"
          
            #Like Peg
            like, created = Like.objects.get_or_create(        
                user_id = request.POST['userid'], 
                board_id = request.POST['boardid'], 
                peg_id = request.POST['pegid']
            )
            if created == False and like is not None:
                like.delete()
            else:
                like.save()
                
            return HttpResponseRedirect('/Pegs/')
           
        
def SharePeg(request):
    return HttpResponse("Feature Coming soon!!!")
  #=============================================================================
  #   if request.method == 'POST':
  #       form = SharePegForm(request.POST)
  #       if form.is_valid():
  #           print "public"
  #           return HttpResponse("Peg Shared")
  #       else:
		#     print "Invalid"
		#     form = SharePegForm()
		#     variables = RequestContext(request, {'form':form})
		#     return render_to_response('Share_peg.html', variables)
  #   else:
		# print "Private"
		# form = SharePegForm()
		# variables = RequestContext(request, {'form':form})
		# return render_to_response('Share_Peg.html', variables)
		#=============================================================================
