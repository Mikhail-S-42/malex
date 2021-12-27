from django.contrib.auth.models import Group
from django.db import models


#--------------------------------------------------------------

class Access(models.Model):
	group = models.ForeignKey(Group,on_delete=models.PROTECT, help_text="Группа")
	start_url = models.CharField(max_length=255, help_text="Стартовая страница")
	access = models.BooleanField(help_text="Доступ")
	account = models.BooleanField(help_text="Профиль")
	devices = models.BooleanField(help_text="Устройства")
	places = models.BooleanField(help_text="Места и АВШ")
	violations = models.BooleanField(help_text="Нарушения")
	transports = models.BooleanField(help_text="Транспорт")
	ppu = models.BooleanField(help_text="ППУ")
	load_violations = models.BooleanField(help_text="Загрузка нарушений")
	file_places = models.BooleanField(help_text="Файл мест установки")
	#-----
	def __str__(self): return '%s - %s' % (self.group, self.start_url)
	#-----
	class Meta:	ordering = ["group"]

#--------------------------------------------------------------