from django.shortcuts import render,render_to_response,RequestContext,HttpResponseRedirect
from PegAPage.models import *
from PegAPage.forms import *
from StdSuites.Type_Names_Suite import null
from django.contrib.auth.models import User
from django.http.response import HttpResponse

# Create your views here.
def load(request):
    listx = [1,2,3,4]
    return render(request, 'CRUDPeg.html',{"listx": listx})


def bookmark_save_page(request):
    if request.method == 'POST':
        form = BookmarkSaveForm(request.POST)
        if form.is_valid():
            # Create or get link.
            link, dummy = UrlLink.objects.get_or_create(
            url=form.cleaned_data['url']
            )
            # Create or get bookmark.
            bookmark, created = Bookmark.objects.get_or_create(
            user=User.objects.get(id=1),
            link=link )
            # Update bookmark title.
            bookmark.title = form.cleaned_data['title']
            # If the bookmark is being updated, clear old tag list.
            if not created:
                bookmark.peg_set.clear()
                # Create new tag list.
            peg_names = form.cleaned_data['pegs'].split()
            for peg_name in peg_names:
                peg, dummy = Peg.objects.get_or_create(name=peg_name)
                bookmark.peg_set.add(peg)
            # Save bookmark to database.
            bookmark.save()
            return HttpResponse("Peg Saved")
        else:
            return HttpResponse("Cannot be blank")
    else:
        form = BookmarkSaveForm()
        variables = RequestContext(request, {'form': form})
        return render_to_response('bookmark_save.html', variables)