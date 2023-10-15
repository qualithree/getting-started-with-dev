AUTHOR = 'QualiThree'
SITENAME = 'Getting Started With Dev'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Australia/Melbourne'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (
    ('CreateCoders', 'https://createcoders.com/'),
    ('QualiThree', 'https://qualithree.com/'),
    ('WhatHashtag.com', 'https://whathashtag.com/'),
)

# Social widget
SOCIAL = (
    ('CreateCoders Instagram', 'https://instagram.com/createcoders'),
    ('CreateCoders Tiktok', 'https://www.tiktok.com/@createcoders'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['./plugins', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
THEME = 'theme/bootstrap-next/'