from django.db import models
from django.contrib.auth.models import User, Group
import uuid

#--------------------------------------------------------------

class Profile(models.Model):
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.ForeignKey(User,on_delete=models.PROTECT, help_text="Пользователь")
	group = models.ForeignKey(Group,on_delete=models.PROTECT, help_text="Группа")
	pos = models.CharField(max_length=255, help_text="Должность")
	sur = models.CharField(max_length=255, help_text="Фамилия")
	name = models.CharField(max_length=255, help_text="Имя")
	mid = models.CharField(max_length=255, help_text="Отчество")	
	city = models.CharField(max_length=255, help_text="Город",null=True)
	addr = models.CharField(max_length=255, help_text="Адрес",null=True)
	tel = models.CharField(max_length=16, help_text="Контактный телефон")
	dateEmploy = models.DateField(help_text="Дата приёма на работу")
	dateDis = models.DateField(null=True, blank=True, help_text="Дата увольнения")
	#------
	def __str__(self):
		str_ = '%s %s %s (%s), Тел: %s, Устроен: %s' % (self.sur, self.name,self.mid,self.pos,self.tel,self.dateEmploy)
		if(not self.dateDis is None): str_ = '%s Уволен: %s' % (str_, self.dateDis)
		return str_
	#------
	class Meta:	ordering = ["sur", "name", "mid"]

#--------------------------------------------------------------