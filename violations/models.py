from django.db import models
from account.models import Profile
from devices.models import Device
import uuid

#---------------------------------------------------------------------------

class Archive(models.Model):
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	device = models.ForeignKey(Device, on_delete=models.PROTECT,  help_text="Прибор")
	operator = models.ForeignKey(Profile,on_delete=models.PROTECT,  help_text="Оператор")
	dateFix = models.DateField(null=True, blank=True, help_text="Дата фиксаций")
	dateGet = models.DateTimeField(help_text="Дата получения")
	dateSend = models.DateTimeField(null=True, blank=True, help_text="Дата отправки")
	amount = models.IntegerField(help_text="Количество нарушений")
	#-----
	def __str__(self):
		str_ = '%s %s Оператор: %s, Нарушений: %s' % (self.dateGet,self.device,self.operator,self.amount)
		if(not self.dateFix is None): str_ = '%s, Дата фиксаций: %s' % (str_,self.dateFix)
		if(not self.dateSend is None): str_ = '%s, Отправлено: %s' % (str_,self.dateSend)
		return str_
	#-----
	class Meta:	ordering = ["dateFix", "device"]

#---------------------------------------------------------------------------

class ErrorType(models.Model):
	name = models.CharField(max_length=255, help_text="Название")
	desc = models.CharField(max_length=1023, help_text="Описание")
	#-----
	def __str__(self): return '%s (%s)' % (self.name,self.desc)
	#-----
	class Meta:	ordering = ["name"]

#---------------------------------------------------------------------------

class Error(models.Model):
	archive = models.ForeignKey('Archive', on_delete=models.PROTECT,  help_text="Архив")
	error = models.ForeignKey('ErrorType', on_delete=models.PROTECT,  help_text="Ошибка")
	#-----
	def __str__(self): return '%s (%s)' % (self.archive,self.error)
	#-----
	class Meta:	ordering = ["archive"]

#---------------------------------------------------------------------------