from .base import *  # NOQA

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += [
    'debug_toolbar',
    # 'pympler',
    # 'debug_toolbar_line_profiler',
    # 'silk',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'silk.middleware.SilkyMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']

# DEBUG_TOOLBAR_PANELS = [
#     # 'djdt_flamegraph.FlamegraphPanel',
#     # 'pympler.panels.MemoryPanel',
#     # 'debug_toolbar_line_profiler.panel.ProfilingPanel',
# ]

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': 'https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js'
}

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
