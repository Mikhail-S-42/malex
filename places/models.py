from django.db import models
from account.models import Profile
import uuid

class Place(models.Model):
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=513, help_text="Название места")
	lat = models.FloatField(help_text="Широта")
	lon = models.FloatField(help_text="Долгота")
	car = models.IntegerField(help_text="Ограничение скорости для легковых")
	truck = models.IntegerField(help_text="Ограничение скорости для грузовых")
	locker = models.ForeignKey('Locker', null=True, blank=True, on_delete=models.SET_NULL, help_text="АВШ")

	def __str__(self): return '%s, Координаты: (%s|%s), Скоростной режим: (%s|%s)' % (self.name,self.lat,self.lon,self.car,self.truck)

	class Meta:	ordering = ["name"]

#---------------------------------------------------------------------------

class Locker(models.Model):
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	num = models.IntegerField(help_text="Номер шкафа")
	place = models.ForeignKey('Place', null=True, blank=True, on_delete=models.SET_NULL, help_text="Место")
	oper = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL, help_text="Ответственный")
	#-----
	def __str__(self):
		str_ = self.num
		if(self.place): str_ = '%s, Место:' % (str_,self.place)
		if(self.oper): str_ = '%s, Оператор:' % (str_,self.oper)
		return str_
	#-----
	class Meta:	ordering = ["place"]

#---------------------------------------------------------------------------