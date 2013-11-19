from django.conf.urls import patterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       (r'^Peg-a-Page/', 'PegAPage.views.loadPeg'),
                       (r'^save/$', 'PegAPage.views.create_peg'),
                       (r'Boards/$', 'PegAPage.views.loadBoard'),
                       (r'Pegs/$', 'PegAPage.views.loadPeg'),
                       (r'Pegs/createPeg/$', 'PegAPage.views.create_peg'),
                       (r'Pegs/deletePeg/$', 'PegAPage.views.deletePeg'),
                       (r'Pegs/updatePeg/$', 'PegAPage.views.updatePeg'),
                       (r'Boards/createBoard/$', 'PegAPage.views.create_board'),
                       (r'Boards/updateBoard/$', 'PegAPage.views.updateBoard'),
                       (r'Boards/deleteBoard/$', 'PegAPage.views.deleteBoard'),
                       (r'Boards/Pegs/commentPeg/$', 'PegAPage.views.commentPeg'),
                       (r'Boards/Pegs/$', 'PegAPage.views.loadPeg'),
                       (r'Pegs/pegitPeg/$', 'PegAPage.views.pegitPeg'),
                       (r'Boards/Pegs/LikePeg/$', 'PegAPage.views.LikePeg'))
