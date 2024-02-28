# Based off microdjango by J. Cliff Dyer
# Get it at https://bitbucket.org/cliff/microdjango/

ROOT_URLCONF = "example_project.urls"
SECRET_KEY = "None"
DEBUG = True
STATIC_URL = "/static/"
SITE_ID = 1

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "./example.db",
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

BOUNCY_TOPIC_ARN = ["arn:aws:sns:us-east-1:250214102493:Demo_App_Unsubscribes"]

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "django_bouncy",
)

MIDDLEWARE = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
        },
    }
]
