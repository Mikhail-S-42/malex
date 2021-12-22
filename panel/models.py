from django.db import models
import uuid

#---------------------------------------------------------------------------

class Position(models.Model):
	name = models.CharField(max_length=255, help_text="Название должности")
	level = models.IntegerField(help_text="Уровень привелегий")

	def __str__(self): return '%s, Level: %s' % (self.name, self.level)

	class Meta:	ordering = ["name"]

#---------------------------------------------------------------------------

class Oper(models.Model):
	sur = models.CharField(max_length=255, help_text="Фамилия")
	name = models.CharField(max_length=255, help_text="Имя")
	mid = models.CharField(max_length=255, help_text="Отчество")
	pos = models.ForeignKey('Position', on_delete=models.PROTECT, help_text="Должность")
	tel = models.CharField(max_length=16, help_text="Контактный телефон")
	employ_date = models.DateField(help_text="Дата приёма на работу")
	dis_date = models.DateField(null=True, blank=True, help_text="Дата увольнения")

	def __str__(self):
		str_ = '%s %s %s (%s), Тел: %s, Устроен: %s' % (self.sur, self.name,self.mid,self.pos,self.tel,self.employ_date)
		if(not self.dis_date is None): str_ = '%s Уволен: %s' % (str_, self.dis_date)
		return str_

	class Meta:	ordering = ["sur", "name", "mid"]

#---------------------------------------------------------------------------

class DeviceStyle(models.Model):
	producer = models.CharField(max_length=255, help_text="Производитель")
	name = models.CharField(max_length=255, help_text="Название")

	def __str__(self): return '%s %s' % (self.name, self.producer)

	class Meta:	ordering = ["producer", "name"]

#---------------------------------------------------------------------------

class Device(models.Model):
	style = models.ForeignKey('DeviceStyle', on_delete=models.PROTECT, help_text="Тип прибора")
	num = models.CharField(max_length=255, help_text="Заводской номер")
	sim = models.CharField(max_length=16, null=True, blank=True, help_text="Номер сим-карты")
	receive_date = models.DateField(help_text="Дата получения")
	return_date = models.DateField(null=True, blank=True, help_text="Дата сдачи")

	def __str__(self):
		str_ = '%s - %s' % (self.style,self.num)
		if(not self.sim is None): str_ = '%s, Сим-карта: %s' % (str_,self.sim)
		str_ = '%s, Получили: %s' % (str_,self.receive_date)
		if(not self.sim is None): str_ = '%s, Сдали: %s' % (str_,self.return_date)
		return str_

	class Meta:	ordering = ["style", "num"]

#---------------------------------------------------------------------------

class HistoryRespons(models.Model):
	device = models.ForeignKey('Device', on_delete=models.PROTECT, help_text="Прибор")
	now_resp = models.ForeignKey('Oper', on_delete=models.PROTECT, help_text="Ответственный", related_name='HistoryRespons_to_Oper_now')
	prew_resp = models.ForeignKey('Oper', null=True, blank=True, on_delete=models.PROTECT, help_text="Предыдущий ответственный", related_name='HistoryRespons_to_Oper_prew')
	next_resp = models.ForeignKey('Oper', null=True, blank=True, on_delete=models.PROTECT, help_text="Следующий ответственный", related_name='HistoryRespons_to_Oper_next')
	begin_date = models.DateTimeField(help_text="Дата получения")
	end_date = models.DateTimeField(null=True, blank=True, help_text="Дата Сдачи")
	
	def __str__(self):
		str_ = '%s - %s' % (self.now_resp,self.device)
		if(not self.prew_resp is None): str_ = '%s, Получил от: %s' % (str_,self.prew_resp)
		if(not self.next_resp is None): str_ = '%s, Передал: %s' % (str_,self.prew_resp)
		str_ = '%s, Дата получения: %s' % (str_,self.begin_date)
		if(not self.end_date is None): str_ = '%s, Дата передачи: %s' % (str_,self.end_date)

	class Meta:	ordering = ["now_resp", "device"]

#---------------------------------------------------------------------------

class ErrorData(models.Model):
	name = models.CharField(max_length=255, help_text="Название ошибки")
	desc = models.CharField(max_length=1023, help_text="Описание ошибки")

	def __str__(self): return '%s (%s)' % (self.name,self.desc)

	class Meta:	ordering = ["name"]

#---------------------------------------------------------------------------

class ArchiveData(models.Model):
	receive_date = models.DateTimeField(help_text="Дата получения")
	send_date = models.DateTimeField(null=True, blank=True, help_text="Дата отправки")
	fix_date = models.DateField(null=True, blank=True, help_text="Дата производства фиксаций")
	device = models.ForeignKey('Device', on_delete=models.PROTECT,  help_text="С какого прибора данные")
	oper = models.ForeignKey('Oper',on_delete=models.PROTECT,  help_text="Оператор кто прислал")
	error = models.ForeignKey('ErrorData', on_delete=models.SET_NULL, null=True, blank=True, help_text="Тип ошибки в данных")
	amount_vi = models.IntegerField(help_text="Количество нарушений")

	def __str__(self):
		str_ = '%s %s Оператор: %s, Нарушений: %s' % (self.receive_date,self.device,self.oper,self.amount_vi)
		if(not self.error is None): str_ = '%s, Ошибка: %s' % (str_,self.error)
		if(not self.fix_date is None): str_ = '%s, Дата фиксаций: %s' % (str_,self.fix_date)
		if(not self.send_date is None): str_ = '%s, Отправлено: %s' % (str_,self.send_date)
		return str_

	class Meta:	ordering = ["receive_date", "device"]

#---------------------------------------------------------------------------

class Place(models.Model):
	name = models.CharField(max_length=513, help_text="Название места")
	lat = models.FloatField(help_text="Широта")
	lon = models.FloatField(help_text="Долгота")
	car = models.IntegerField(help_text="Ограничение скорости для легковых")
	truck = models.IntegerField(help_text="Ограничение скорости для грузовых")

	def __str__(self): return '%s, Координаты: (%s|%s), Скоростной режим: (%s|%s)' % (self.name,self.lat,self.lon,self.car,self.truck)

	class Meta:	ordering = ["name"]

#---------------------------------------------------------------------------

class Locker(models.Model):
	num = models.IntegerField(help_text="Номер шкафа")
	place = models.ForeignKey('Place', null=True, blank=True, on_delete=models.SET_NULL, help_text="Место установки")
	oper = models.ForeignKey('Oper', null=True, blank=True, on_delete=models.SET_NULL, help_text="Ответственный сотрудник")

	def __str__(self):
		str_ = self.num
		if(self.place): str_ = '%s, Место:' % (str_,self.place)
		if(self.oper): str_ = '%s, Оператор:' % (str_,self.oper)
		return str_

	class Meta:	ordering = ["place"]

#---------------------------------------------------------------------------

class MasterRepair(models.Model):
	comp = models.CharField(max_length=255, help_text="Название компании")
	name = models.CharField(max_length=255, help_text="ФИО мастера проводившего ремонт")

	def __str__(self): return '%s (%s)' % (self.comp,self.name)

	class Meta:	ordering = ["comp", "name"]

#---------------------------------------------------------------------------

class Repair(models.Model):
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	device = models.ForeignKey('Device', on_delete=models.PROTECT, help_text="Прибор")
	start_date = models.DateField(null=True, blank=True, help_text="Дата начала ремонта")
	end_date = models.DateField(null=True, blank=True, help_text="Дата конца ремонта")
	who = models.ForeignKey('MasterRepair', on_delete=models.PROTECT, help_text="Мастер производивший ремонт")
	warranty = models.BooleanField(null=True, blank=True, help_text="Гарантия")
	cause = models.CharField(max_length=511, help_text="Причина")
	diag = models.CharField(max_length=511, help_text="Выявлено при диагностики")
	price = models.DecimalField(null=True, blank=True, max_digits=9, decimal_places=2, help_text="Цена ремонта")

	def __str__(self):
		str_ =  '%s %s' % (self.start_date,self.device)
		if(not self.end_date is None): str_ =  '%s, Завершено:%s' % (str_,self.end_date)
		if(self.warranty): str_ =  '%s, Гарантия: Да' % str_
		else: str_ =  '%s, Гарантия: Нет' % str_
		str_ =  '%s, Причина:%s' % (str_,self.cause)
		str_ =  '%s, Диагностика:%s' % (str_,self.diag)
		if(not self.end_date is None): str_ =  '%s, Цена:%s' % (str_,self.price)

	class Meta:	ordering = ["-start_date", "device"]

#---------------------------------------------------------------------------

class TypeRepair(models.Model):
	name = models.CharField(max_length=255, help_text="Типа ремонта")

	def __str__(self): return '%s' % self.name

	class Meta:	ordering = ["name"]

#---------------------------------------------------------------------------

class Part(models.Model):
	name = models.CharField(max_length=255, help_text="Запасная часть")
	desc = models.CharField(max_length=511, help_text="Описание запасной части")

	def __str__(self): return '%s (%s)' % (self.name,self.desc)

	class Meta:	ordering = ["name"]

#---------------------------------------------------------------------------

class DoneRepair(models.Model):
	repair = models.ForeignKey('Repair',on_delete=models.PROTECT,  help_text="Ремонт")
	typeRepair = models.ForeignKey('TypeRepair', on_delete=models.PROTECT, help_text="Тип ремонта")
	desc = models.CharField(max_length=511, null=True, blank=True, help_text="Описание")
	part = models.ForeignKey('Part', on_delete=models.SET_NULL, null=True, blank=True, help_text="Название запчасти")

	def __str__(self):
		str_ =  '%s - %s:' % (self.repair,self.typeRepair)
		if(not self.desc is None): str_ = '%s %s' % (str_,self.desc)
		if(not self.part is None): str_ = '%s %s' % (str_,self.part)
		return str_

	class Meta:	ordering = ["repair"]

#---------------------------------------------------------------------------