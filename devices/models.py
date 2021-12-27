import uuid
from django.db import models
from account.models import Profile
import uuid

#--------------------------------------------------------------

class DeviceType(models.Model):
	style = models.CharField(max_length=255, help_text="Тип")	
	#-----
	def __str__(self): return '%s' % self.style
	#-----
	class Meta:	ordering = ["style"]

#--------------------------------------------------------------

class DeviceModel(models.Model):
	style = models.ForeignKey('DeviceType',on_delete=models.PROTECT, help_text="Тип устройства")	
	mark = models.CharField(max_length=255, help_text="Производитель")
	model = models.CharField(max_length=255, help_text="Модель")
	#-----
	def __str__(self): return '%s: %s - %s' % (self.style,self.mark,self.model)
	#-----
	class Meta:	ordering = ["style", "mark", "model"]

#--------------------------------------------------------------

class Device(models.Model):
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	devModel = models.ForeignKey('DeviceModel',on_delete=models.PROTECT, help_text="Модель устройства")
	sn = models.CharField(max_length=512, help_text="Серийный номер", null=True, blank=True)
	sim = models.CharField(max_length=16, null=True, blank=True, help_text="Номер сим-карты")
	date = models.DateField(help_text="Дата получения")
	dateEnd = models.DateField(null=True, blank=True, help_text="Дата сдачи")
	#-----
	def __str__(self):
		str_ = '%s - S/N: %s' % (self.devModel,self.sn)
		if(not self.sim is None): str_ = '%s, Сим-карта: %s' % (str_,self.sim)
		str_ = '%s, Получили: %s' % (str_,self.date)
		if(not self.sim is None): str_ = '%s, Сдали: %s' % (str_,self.dateEnd)
		return str_
	#-----
	class Meta:	ordering = ["devModel", "sn"]

#--------------------------------------------------------------

class HistoryRespons(models.Model):
	device = models.ForeignKey('Device', on_delete=models.PROTECT, help_text="Устройство")
	owner = models.ForeignKey(Profile, on_delete=models.PROTECT, help_text="Ответственный", related_name='HistoryResponsOwner')
	prewOwner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.PROTECT, help_text="Предыдущий ответственный", related_name='HistoryResponsOwnerPrew')
	nextOwner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.PROTECT, help_text="Следующий ответственный", related_name='HistoryResponsOwnerNext')
	dateBegin = models.DateTimeField(help_text="Дата получения")
	dateEnd = models.DateTimeField(null=True, blank=True, help_text="Дата передачи")
	#-----
	def __str__(self):
		str_ = '%s - %s' % (self.owner,self.device)
		if(not self.prewOwner is None): str_ = '%s, Получил от: %s' % (str_,self.prewOwner)
		if(not self.nextOwner is None): str_ = '%s, Передал: %s' % (str_,self.nextOwner)
		str_ = '%s, Дата получения: %s' % (str_,self.dateBegin)
		if(not self.dateEnd is None): str_ = '%s, Дата передачи: %s' % (str_,self.dateEnd)
	#-----
	class Meta:	ordering = ["owner", "device"]

#--------------------------------------------------------------

class MasterRepair(models.Model):
	comp = models.CharField(max_length=255, help_text="Название компании")
	name = models.CharField(max_length=255, help_text="ФИО мастера проводившего ремонт")
	#-----
	def __str__(self): return '%s (%s)' % (self.comp,self.name)
	#-----
	class Meta:	ordering = ["comp", "name"]

#---------------------------------------------------------------------------

class Repair(models.Model):
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	device = models.ForeignKey('Device', on_delete=models.PROTECT, help_text="Устройство")
	dateBegin = models.DateField(null=True, blank=True, help_text="Дата начала ремонта")
	dateEnd = models.DateField(null=True, blank=True, help_text="Дата конца ремонта")
	master = models.ForeignKey('MasterRepair', on_delete=models.PROTECT,null=True, blank=True, help_text="Мастер производивший ремонт")
	warranty = models.BooleanField(null=True, blank=True, help_text="Гарантия")
	cause = models.CharField(max_length=511, help_text="Причина")
	diag = models.CharField(max_length=511, help_text="Выявлено при диагностики")
	price = models.DecimalField(null=True, blank=True, max_digits=9, decimal_places=2, help_text="Цена ремонта")
	#-----
	def __str__(self):
		str_ =  '%s %s' % (self.dateBegin,self.device)
		if(not self.dateEnd is None): str_ =  '%s, Завершено:%s' % (str_,self.dateEnd)
		if(self.warranty): str_ =  '%s, Гарантия: Да' % str_
		else: str_ =  '%s, Гарантия: Нет' % str_
		str_ =  '%s, Причина:%s' % (str_,self.cause)
		str_ =  '%s, Диагностика:%s' % (str_,self.diag)
		if(not self.end_date is None): str_ =  '%s, Цена:%s' % (str_,self.price)
	#-----
	class Meta:	ordering = ["-dateBegin", "device"]

#---------------------------------------------------------------------------

class TypeRepair(models.Model):
	name = models.CharField(max_length=255, help_text="Типа ремонта")
	#-----
	def __str__(self): return '%s' % self.name
	#-----
	class Meta:	ordering = ["name"]

#---------------------------------------------------------------------------

class Part(models.Model):
	name = models.CharField(max_length=255, help_text="Запасная часть")
	desc = models.CharField(max_length=511, help_text="Описание запасной части")
	#-----
	def __str__(self): return '%s (%s)' % (self.name,self.desc)
	#-----
	class Meta:	ordering = ["name"]

#---------------------------------------------------------------------------

class DoneRepair(models.Model):
	repair = models.ForeignKey('Repair',on_delete=models.PROTECT,  help_text="Ремонт")
	typeRepair = models.ForeignKey('TypeRepair', on_delete=models.PROTECT, help_text="Тип ремонта")
	desc = models.CharField(max_length=511, null=True, blank=True, help_text="Описание")
	part = models.ForeignKey('Part', on_delete=models.SET_NULL, null=True, blank=True, help_text="Название запчасти")
	#-----
	def __str__(self):
		str_ =  '%s - %s:' % (self.repair,self.typeRepair)
		if(not self.desc is None): str_ = '%s %s' % (str_,self.desc)
		if(not self.part is None): str_ = '%s %s' % (str_,self.part)
		return str_
	#-----
	class Meta:	ordering = ["repair"]

#---------------------------------------------------------------------------