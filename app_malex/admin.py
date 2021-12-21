from django.contrib import admin
from .models import Position, Oper, DeviceStyle, Device, HistoryRespons, ErrorData, ArchiveData, Place, Locker, MasterRepair, Repair, TypeRepair, Part, DoneRepair

admin.site.register(Position)
admin.site.register(Oper)
admin.site.register(DeviceStyle)
admin.site.register(Device)
admin.site.register(HistoryRespons)
admin.site.register(ErrorData)
admin.site.register(ArchiveData)
admin.site.register(Place)
admin.site.register(Locker)
admin.site.register(MasterRepair)
admin.site.register(Repair)
admin.site.register(TypeRepair)
admin.site.register(Part)
admin.site.register(DoneRepair)