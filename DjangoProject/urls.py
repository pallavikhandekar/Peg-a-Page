from django.conf.urls import patterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       (r'^Peg-a-Page/', 'PegAPage.views.loadPeg'),
                       (r'^save/$', 'PegAPage.views.create_peg'),
                       (r'Pegs/$', 'PegAPage.views.loadPeg'),
                       (r'PegsUI/$', 'PegAPage.views.loadUI'), 
                       (r'Pegs/createPeg/$', 'PegAPage.views.create_peg'),
                       (r'Pegs/deletePeg/$', 'PegAPage.views.deletePeg'),
                       (r'Pegs/updatePeg/$', 'PegAPage.views.updatePeg'),
                       (r'Pegs/createBoard/$', 'PegAPage.views.create_board'),
                       (r'Pegs/commentPeg/$', 'PegAPage.views.commentPeg'),
                       (r'Pegs/pegitPeg/$', 'PegAPage.views.pegitPeg'))