DATABASE_ENGINE = "sqlite3"

SECRET_KEY = "abcd123"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "./example.db",
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

INSTALLED_APPS = ("django_bouncy",)

BOUNCY_TOPIC_ARN = ["arn:aws:sns:us-east-1:250214102493:Demo_App_Unsubscribes"]
