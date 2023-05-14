from django.contrib import admin

# Register your models here.
from probes.models import Probe, ProbeInst

admin.site.register(Probe)
admin.site.register(ProbeInst)