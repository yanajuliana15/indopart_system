from django.contrib import admin
from .models import Machine, Sparepart, JadwalPreventive, Breakdown

admin.site.register(Machine)
admin.site.register(Sparepart)
admin.site.register(JadwalPreventive)
admin.site.register(Breakdown)