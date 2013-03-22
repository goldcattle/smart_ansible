# Django settings for indivo_problems project.

## PARAMETERS TO REVIEW

APP_HOME = "{{path_to_smart_sample_apps}}"

SMART_APP_SERVER_BASE = '{{app_server_base_url}}'
SMART_API_SERVER_BASE = '{{api_server_base_url}}'

AC_OAUTH = {
  'consumer_key': 'allergy-check@apps.smartplatforms.org', 
  'consumer_secret': 'smartapp-secret'
}

SS_OAUTH = {
  'consumer_key': 'smart-connector@apps.smartplatforms.org', 
  'consumer_secret': 'smartapp-secret'
}

####
#### Below here probably doesn't need modification
####

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS
DATABASE_RXN = 'rxnorm'
DATABASE_USER = 'smart'             # Not used with sqlite3.
DATABASE_PASSWORD = 'smart'             # Not used with sqlite3.

DATABASE_ENGINE = ''           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = ''             # Or path to database file if using sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'e7^o7-%74eov^a!&9=9&)()%&_4%!bv*@01&z+^z&36@nnj=7w'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'smart_sample_apps.middlewares.exception.ExceptionMiddleware'
)

ROOT_URLCONF = 'smart_sample_apps.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    APP_HOME + "/templates"
)

CONCURRENT_THREADING = False

INSTALLED_APPS = (
    'django_concurrent_test_server',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
)

# sessions in filesystem
SESSION_ENGINE = 'django.contrib.sessions.backends.file'

SESSION_FILE_PATH = APP_HOME + "/session"

