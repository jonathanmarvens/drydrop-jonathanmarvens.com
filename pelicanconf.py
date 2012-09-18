#!/usr/bin/env python

# Basic settings
ARTICLE_DIR					= 'posts'
ARTICLE_EXCLUDES			= ('pages', 'static/public')
AUTHOR						= u'jonathanmarvens'
DATE_FORMATS				= {}
DEFAULT_CATEGORY			= 'uncategorized'
DEFAULT_DATE				= 'fs'
DEFAULT_DATE_FORMAT			= '%a., %B %d, %Y'
DELETE_OUTPUT_DIRECTORY		= False
DIRECT_TEMPLATES			= ('index', 'tags', 'categories', 'archives', '404')
DISPLAY_PAGES_ON_MENU 		= False
JINJA_EXTENSIONS			= []
LESS_GENERATOR				= False
LOCALE						= ''
MARKUP						= ('md', 'rst')
MD_EXTENSIONS				= ['codehilite', 'extra']
OUTPUT_PATH					= 'application'
PAGE_DIR					= 'pages'
PAGE_EXCLUDES				= ('posts', 'static/public')
PAGINATED_DIRECT_TEMPLATES	= ('index', 'archives')
PATH						= None
PDF_GENERATOR				= False
PLUGINS						= []
RELATIVE_URLS				= True
SITENAME					= u'jonathanmarvens.com'
SITEURL						= 'http://www.jonathanmarvens.com'
STATIC_PATHS				= ['public']
SUMMARY_MAX_LENGTH			= 25
TIMEZONE					= 'America/New_York'
TYPOGRIFY					= True

# URL settings
## ARTICLE_LANG_SAVE_AS	= 'posts/{lang}/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
## ARTICLE_LANG_URL		= 'posts/{lang}/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
## ARTICLE_SAVE_AS		= 'posts/en/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
## ARTICLE_URL			= 'posts/en/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
## AUTHOR_SAVE_AS		= 'authors/{name}/index.html'
## AUTHOR_URL			= 'authors/{name}/'
## CATEGORY_SAVE_AS		= 'categories/{name}/index.html'
## CATEGORY_URL			= 'categories/{name}/'
## PAGE_LANG_SAVE_AS	= 'pages/{lang}/{slug}/index.html'
## PAGE_LANG_URL		= 'pages/{lang}/{slug}/'
## PAGE_SAVE_AS			= 'pages/en/{slug}/index.html'
## PAGE_URL				= 'pages/en/{slug}/'
## TAG_SAVE_AS			= 'tags/{name}/index.html'
## TAG_URL				= 'tags/{name}/'
### ---------- ### ---------- ### ---------- ### ---------- ###
ARTICLE_LANG_SAVE_AS	= 'posts/{lang}/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_LANG_URL		= ARTICLE_LANG_SAVE_AS
ARTICLE_SAVE_AS			= 'posts/en/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_URL				= ARTICLE_SAVE_AS
AUTHOR_SAVE_AS			= 'authors/{name}.html'
AUTHOR_URL				= AUTHOR_SAVE_AS
CATEGORY_SAVE_AS		= 'categories/{name}.html'
CATEGORY_URL			= CATEGORY_SAVE_AS
PAGE_LANG_SAVE_AS		= 'pages/{lang}/{slug}.html'
PAGE_LANG_URL			= PAGE_LANG_SAVE_AS
PAGE_SAVE_AS			= 'pages/en/{slug}.html'
PAGE_URL				= PAGE_SAVE_AS
TAG_SAVE_AS				= 'tags/{name}.html'
TAG_URL					= TAG_SAVE_AS

# Feed settings
CATEGORY_FEED_ATOM	= 'feeds/category.%s.atom.xml'
CATEGORY_FEED_RSS	= 'feeds/category.%s.rss'
FEED_ATOM			= 'feeds/all.en.atom.xml'
FEED_DOMAIN			= SITEURL
FEED_MAX_ITEMS		= 25
FEED_RSS			= 'feeds/all.en.rss'
TAG_FEED_ATOM		= 'feeds/tag.%s.atom.xml'
TAG_FEED_RSS		= 'feeds/tag.%s.rss'

# Pagination settings
DEFAULT_ORPHANS		= 0
DEFAULT_PAGINATION	= 10

# Tag cloud settings
TAG_CLOUD_STEPS		= 5
TAG_CLOUD_MAX_ITEMS	= 25

# Translation settings
DEFAULT_LANG		= 'en'
TRANSLATION_FEED	= 'feeds/all.%s.atom.xml'

# Content ordering settings
NEWEST_FIRST_ARCHIVES	= True
REVERSE_CATEGORY_ORDER	= False

# Theme settings
CSS_FILE			= 'main.css'
THEME				= 'jonathanmarvens-custom-1'
THEME_STATIC_PATHS	= ['static']
WEBASSETS			= True

# Theme development settings
## DISQUS_SITENAME		= 'jonathanmarvens-com'
## GITHUB_URL
## GOOGLE_ANALYTICS
## GOSQUARED_SITENAME
## LINKS
## MENUITEMS
## PIWIK_SITE_ID
## PIWIK_SSL_URL
## PIWIK_URL
## SOCIAL
TWITTER_USERNAME	= 'jonathanmarvens'
LIVEFYRE_SITE_ID	= 312164

# Miscellaneous settings
FILES_TO_COPY	= ()

# Personal settings
EXTRA_SITE_AUTHOR			= u'Jonathan Marvens Barronville'
EXTRA_SITE_DESCRIPTION	= (
	u'This is the online home of %(author)s. Feel free to navigate around. Make yourself at home.' % {
		'author': EXTRA_SITE_AUTHOR
	}
)

def custom_filter_datetime_format (date_and_time, date_format):
	from datetime import datetime

	return datetime.strptime(date_and_time, '%Y-%m-%d %H:%M:%S').strftime(date_format)

JINJA_FILTERS = {
	'format_date_and_time': custom_filter_datetime_format,
}