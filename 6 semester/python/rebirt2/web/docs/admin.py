import sys

from django.contrib import admin
sys.path.append("..")
from .models import GeneralDocument

admin.site.register(GeneralDocument)
