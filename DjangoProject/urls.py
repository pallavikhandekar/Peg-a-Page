from django.conf.urls import patterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from PegAPage.views import *
from django.views.generic import TemplateView

import os.path
site_media = os.path.join(os.path.dirname(__file__), 'site_media')

admin.autodiscover()

urlpatterns = patterns('',
                       (r'^Peg-a-Page/', 'PegAPage.views.loadPeg'),
                       (r'^save/$', 'PegAPage.views.create_peg'),
                       (r'Boards/$', 'PegAPage.views.loadBoard'),
                       (r'Pegs/$', 'PegAPage.views.loadPeg'),
                       (r'Pegs/createPeg/$', 'PegAPage.views.create_peg'),
                       (r'Pegs/deletePeg/$', 'PegAPage.views.deletePeg'),
                       (r'Pegs/updatePeg/$', 'PegAPage.views.editPeg'),
                       (r'Boards/createBoard/$', 'PegAPage.views.create_board'),
                       (r'Boards/updateBoard/$', 'PegAPage.views.updateBoard'),
                       (r'Boards/deleteBoard/$', 'PegAPage.views.deleteBoard'),
                       (r'Boards/Pegs/commentPeg/$', 'PegAPage.views.commentPeg'),
                       (r'Boards/Pegs/$', 'PegAPage.views.loadPeg'),
                       (r'Pegs/pegitPeg/$', 'PegAPage.views.pegitPeg'),
                       (r'Pegs/LikePeg/$', 'PegAPage.views.LikePeg'),
                       (r'^login/$', 'django.contrib.auth.views.login'),
                       (r'^logout/$', logout_page),
                       (r'^register/$', register_page),
                       (r'^register/success/$', TemplateView.as_view(template_name='registration/register_success.html')),
                       (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': site_media }),
                       (r'^ContactMe/$', contactMe_page),
                       (r'^PrivacyPolicy/$', privacyPolicy_page),
                       (r'Pegs/SharePeg/$', 'PegAPage.views.SharePeg'),
                       )




