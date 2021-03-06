"""CMS apphook for the ``multilingual_news`` app."""
from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class MultilingualNewsApphook(CMSApp):
    name = _("Multilingual News Apphook")
    urls = ["multilingual_news.urls"]
    app_name = "multilingual_news" 

apphook_pool.register(MultilingualNewsApphook)
