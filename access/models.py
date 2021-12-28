from django.contrib.auth.models import Group
from django.db import models


#--------------------------------------------------------------

class Access(models.Model):
	group = models.ForeignKey(Group,on_delete=models.PROTECT, help_text="Группа")
	startUrl = models.CharField(max_length=255, help_text="Стартовая страница")
	access = models.BooleanField(help_text="Настройка доступа")
	devices = models.BooleanField(help_text="Устройства")
	places = models.BooleanField(help_text="Места и АВШ")
	violations = models.BooleanField(help_text="Нарушения")
	transports = models.BooleanField(help_text="Транспорт")
	ppu = models.BooleanField(help_text="ППУ")
	loadViolations = models.BooleanField(help_text="Загрузка нарушений")
	filePlaces = models.BooleanField(help_text="Файл мест установки")
	#-----
	def __str__(self): return '%s - %s' % (self.group, self.startUrl)
	#-----
	class Meta:	ordering = ["group"]

#--------------------------------------------------------------