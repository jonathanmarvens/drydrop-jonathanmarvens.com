# #!/usr/bin/env python
# # -*- coding: utf-8 -*- #

# AUTHOR = u"Jonathan Marvens Barronville"
# SITENAME = u"jonathanmarvens.com"
# SITEURL = ''

# TIMEZONE = 'America/New_York'

# DEFAULT_LANG = 'en'

# # Blogroll
# LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
#           ('Python.org', 'http://python.org'),
#           ('Jinja2', 'http://jinja.pocoo.org'),
#           ('You can modify those links in your config file', '#'),)

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

# DEFAULT_PAGINATION = 10

ARTICLE_DIR					= 'posts'
ARTICLE_EXCLUDES			= ('pages')
ARTICLE_LANG_SAVE_AS		= 'posts/{lang}/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_LANG_URL			= 'posts/{lang}/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS				= 'posts/en/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_URL					= 'posts/en/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
AUTHOR						= u'Jonathan Marvens Barronville'
AUTHOR_SAVE_AS				= 'authors/{name}/index.html'
AUTHOR_URL					= 'authors/{name}/'
CATEGORY_FEED_ATOM			= 'feeds/category.%s.atom.xml'
CATEGORY_FEED_RSS			= 'feeds/category.%s.rss'
CATEGORY_SAVE_AS			= 'categories/{name}/index.html'
CATEGORY_URL				= 'categories/{name}/'
CSS_FILE					= 'main.css'
DATE_FORMATS				= {}
DEFAULT_CATEGORY			= 'uncategorized'
DEFAULT_DATE				= 'fs'
DEFAULT_DATE_FORMAT			= '%a %d %B %Y'
DEFAULT_LANG				= 'en'
DEFAULT_ORPHANS				= 0
DEFAULT_PAGINATION			= 10
DELETE_OUTPUT_DIRECTORY		= False
DIRECT_TEMPLATES			= ('index', 'tags', 'categories', 'archives')
DISPLAY_PAGES_ON_MENU 		= False
FEED_ATOM					= 'feeds/all-en.atom.xml'
FEED_DOMAIN					= SITEURL
FEED_MAX_ITEMS				= 25
FEED_RSS					= 'feeds/all-en.rss'
JINJA_EXTENSIONS			= []
LESS_GENERATOR				= True
LOCALE						= ''
MARKUP						= ('md', 'rst')
MD_EXTENSIONS				= ['codehilite', 'extra']
NEWEST_FIRST_ARCHIVES		= True
OUTPUT_PATH					= 'application/'
PAGE_DIR					= 'pages'
PAGE_EXCLUDES				= ('posts')
PAGE_LANG_SAVE_AS			= 'pages/{lang}/{slug}/index.html'
PAGE_LANG_URL				= 'pages/{lang}/{slug}/'
PAGE_SAVE_AS				= 'pages/en/{slug}/index.html'
PAGE_URL					= 'pages/en/{slug}/'
PAGINATED_DIRECT_TEMPLATES	= ('index', 'archives')
PATH						= None
PDF_GENERATOR				= False
PLUGINS						= []
RELATIVE_URLS				= True
REVERSE_CATEGORY_ORDER		= False
SITENAME					= u'jonathanmarvens.com | Home of Jonathan Barronville'
SITEURL						= 'http://www.jonathanmarvens.com'
STATIC_PATHS				= ['public']
SUMMARY_MAX_LENGTH			= 25
TAG_CLOUD_STEPS				= 5
TAG_CLOUD_MAX_ITEMS			= 25
TAG_FEED_ATOM				= 'feeds/tag.%s.atom.xml'
TAG_FEED_RSS				= 'feeds/tag.%s.rss'
TAG_SAVE_AS					= 'tags/{name}/index.html'
TAG_URL						= 'tags/{name}/'
THEME						= 'simple'
THEME_STATIC_PATHS			= ['static']
TIMEZONE					= 'America/New_York'
TRANSLATION_FEED			= 'feeds/all-%s.atom.xml'
TYPOGRIFY					= True
WEBASSETS					= True