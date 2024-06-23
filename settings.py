LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{asctime} {levelname} {message} {pathname}",
            "style": "{",
        },
        "simple": {
            "format": "{asctime} {levelname} {message}",
            "style": "{",
        },

        "extra": {
            "format": "{asctime} {levelname} {message} {pathname} {exc_info}",
            "style": "{",
        },
            
        "filing": {
            "format": "{asctime} {levelname} {module} {message}",
            "style": "{",  
        },
    },

    "filters": {
        "special": {
            "()": "project.logging.SpecialFilter",
            "foo": "bar",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },

        "console_warning": {
            "level": "WARNING",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },

        "console_error": {
            "level": "ERROR",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "extra",
        },

        "file_general": {
            "level": "INFO",
            "filters": ["require_debug_false"],
            "class": "logging.FileHandler",
            "filename": "/path/to/django/general.log",
            "formatter": "filing",
        },

        "file_error": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "logging.FileHandler",
            "filename": "/path/to/django/errors.log",
            "formatter": "extra",
        },
        
        "file_security": {
            "level": "WARNING",
            "filters": ["require_debug_false"],
            "class": "logging.FileHandler",
            "filename": "/path/to/django/security.log",
            "formatter": "filing",
        },

        "mail_admins": {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            "filters": ["require_debug_false"],
            "formatter": "verbose",
        },

        
    },
    "loggers": {
        "django": {
            "level": "DEBUG"
            "handlers": ["console", "console_warning", "console_error", "file_general"],
            "propagate": True,
        },
        "django.request": {
            "handlers": ["file_error", "mail_admins"],
            "propagate": True,
        },
        "django.security": {
            "handlers": ["file_security"],
            "level": "INFO",
            "propagate": True,
        },
        "django.server": {
            "handlers": ["file_security", "file_error", "mail_admins"],
            "propagate": True,
            "filters": ["special"],
        },
        "django.template": {
            "handlers": ["file_error"],
            "propagate": True,
        },
         "django.db.backends": {
            "handlers": ["file_error"],
            "propagate": True,
        },
    },
}
