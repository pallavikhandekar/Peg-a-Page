from django.conf.urls import patterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       (r'^DjangoProject/', 'PegAPage.views.load'),
                       (r'^save/$', 'PegAPage.views.create_bookmarks'),
                       (r'Pegs/$', 'PegAPage.views.loadPeg'),
                       (r'Pegs/createPeg/$', 'PegAPage.views.create_bookmarks'),
                       (r'Pegs/deletePeg/$', 'PegAPage.views.deletePeg'))