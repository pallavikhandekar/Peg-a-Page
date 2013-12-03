from PegAPage.models import *
'''
Created on Nov 25, 2013

@author: pallavi
'''
def getPegsForBoard(boardid):
    board = Board.objects.get(id=boardid)
    pegs =board.peg_set.all() 
    return pegs

def modifyPeg(url,name,desc,pegid):
    peg = Peg.objects.get(id= pegid)
    peg.url = url
    peg.name = name
    peg.peg_des = desc
    peg.save()
    
def savePeg(form,boardid):
    # Create Peg
    peg, dummy = Peg.objects.get_or_create(
    url = form.cleaned_data['url'],
    name = form.cleaned_data['name'],
    peg_des = form.cleaned_data['desc']
    )
    myboard = Board.objects.get(id = boardid)
    #boardname = request.POST['boardname']
    myboard.peg_set.add(peg)
    myboard.save()
    
def removePegforBoard(boardid,pegid):
    board = Board.objects.get(id=boardid)
    peg = Peg.objects.get(id= pegid)
    board.peg_set.remove(peg)
    board.save()
    
def removePeg(pegid):
    peg = Peg.objects.get(id= pegid)
    peg.delete()
    
def getBoard(boardid):
    return Board.objects.get(id=boardid)

def getBoardsForUser(userid):
    boards = Board.objects.all().filter(user = userid)  
    return boards

def saveboard(form,userid):
    board, dummy = Board.objects.get_or_create(
                Board_name = form.cleaned_data['name'],
                user_id = userid,                
                Board_des = form.cleaned_data['desc']
            )
    Board.save(board)
    
def removeboard(boardid):
    board = Board.objects.get(id=boardid)  
    Peg.objects.filter(boards = boardid).delete()       
    board.delete()    
    print "delete"
    
def updateboard(boardid,name,desc):
    board = Board.objects.get(id= boardid)   
    board.Board_name = name
    board.Board_des = desc
    board.save()
    print desc
    print "update"
