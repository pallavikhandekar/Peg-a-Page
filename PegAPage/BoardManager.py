from PegAPage.models import *
'''
Created on Dec 1, 2013

@author: sharanya
'''

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
