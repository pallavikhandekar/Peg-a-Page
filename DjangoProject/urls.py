from django.conf.urls import patterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       (r'^DjangoProject/', 'PegAPage.views.load'),
                       (r'^save/$', 'PegAPage.views.bookmark_save_page'),
                       (r'^createPeg/$', 'PegAPage.views.bookmark_save_page'),
                       (r'^Pegs/$', 'PegAPage.views.loadPeg'))