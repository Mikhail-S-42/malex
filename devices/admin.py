from django.contrib import admin
from .models import DeviceType, DeviceModel, Device, HistoryRespons, MasterRepair, Repair, TypeRepair, Part, DoneRepair

admin.site.register(DeviceType)
admin.site.register(DeviceModel)
admin.site.register(Device)
admin.site.register(HistoryRespons)
admin.site.register(MasterRepair)
admin.site.register(Repair)
admin.site.register(TypeRepair)
admin.site.register(Part)
admin.site.register(DoneRepair)
