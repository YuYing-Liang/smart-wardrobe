from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings
from django.urls import reverse
from django.utils.timezone import template_localtime
from jinja2 import Environment


# In testing, nothing in this file can be overwritten using the
# @patch or @override_settings decorators, because it is evaluated before
# the test methods. If you have tests that rely on these values, explicitly
# set them in the context of your views.


def environment(**options):
    env = Environment(**options)
    env.globals.update(
        {
            # Functions
            "static": staticfiles_storage.url,
            "url": reverse,
            "localtime": template_localtime,
        }
    )
    return env
