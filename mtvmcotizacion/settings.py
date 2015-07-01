"""
Django settings for mtvmcotizacion project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z)sr!is=6dk1x82ajleb$wbqmen^cyrb1_jb7xjw0385mfzb%8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Redirect when login is correct.
LOGIN_REDIRECT_URL = "/home"
# Redirect when login is not correct.
LOGIN_URL = '/'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'direccion',
    'cliente',
    'telefono',
    'ambiente',
    'servicio',
    'mueble',
    'contenido',
    'trabajador',
    'cotizacion',
    'inicio',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

)

# Es una secuencia de valores agrupados llamados procesadores
# de contexto - que tienen un objeto de solicitud
# como su argumento y devuelven un diccionario de temas que se
# fusionó con el contexto
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request'
)

ROOT_URLCONF = 'mtvmcotizacion.urls'

WSGI_APPLICATION = 'mtvmcotizacion.wsgi.application'

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'template').replace('\\', '/'), )

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_mtvmcotizacion',
        'USER': 'root',
        'PASSWORD': 'md123',
        'HOST': '',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

USE_TZ = True

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

# Configuraciones referidas al formato de fechas, horas y números
# USE_L10N Indica si el formato local será utilizado o no

USE_L10N = True

USE_THOUSAND_SEPARATOR = True

NUMBER_GROUPING = 3

DATE_INPUT_FORMATS = (
    '%d-%m-%Y', '%d/%m/%Y',              # '25-10-2006', '25/10/2006'
    '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y',  # '2006-10-25', '10/25/2006', '10/25/06'
    '%b %d %Y', '%b %d, %Y',             # 'Oct 25 2006', 'Oct 25, 2006'
    '%d %b %Y', '%d %b, %Y',             # '25 Oct 2006', '25 Oct, 2006'
    '%B %d %Y', '%B %d, %Y',             # 'October 25 2006', 'October 25, 2006'
    '%d %B %Y', '%d %B, %Y',             # '25 October 2006', '25 October, 2006'
)

DATETIME_INPUT_FORMATS = (
    '%d-%m-%Y %H:%M:%S',     # '25-10-2006 14:30:59'
    '%d-%m-%Y %H:%M:%S.%f',  # '25-10-2006 14:30:59.000200'
    '%d-%m-%Y %H:%M',        # '25-10-2006 14:30'
    '%d-%m-%Y,'              # '25-10-2006'
    '%Y-%m-%d %H:%M:%S',     # '25/10/2006 14:30:59'
    '%Y-%m-%d %H:%M:%S.%f',  # '25/10/2006 14:30:59.000200'
    '%Y-%m-%d %H:%M',        # '25/10/2006 14:30'
    '%Y-%m-%d',              # '25/10/2006'
    '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
    '%Y-%m-%d %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
    '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
    '%Y-%m-%d',              # '2006-10-25'
    '%m/%d/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
    '%m/%d/%Y %H:%M:%S.%f',  # '10/25/2006 14:30:59.000200'
    '%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
    '%m/%d/%Y',              # '10/25/2006'
    '%m/%d/%y %H:%M:%S',     # '10/25/06 14:30:59'
    '%m/%d/%y %H:%M:%S.%f',  # '10/25/06 14:30:59.000200'
    '%m/%d/%y %H:%M',        # '10/25/06 14:30'
    '%m/%d/%y',              # '10/25/06'
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = ''

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    )
