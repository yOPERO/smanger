from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Location(models.Model):
	officeLocation = models.CharField(max_length=50)
	def __str__(self):
		return self.officeLocation

	class Meta:
		ordering = ('officeLocation',)

class Screen(models.Model):
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	brand = models.CharField(max_length=30)
	model = models.CharField(max_length=30)

	# def save(self, *args, **kwargs):
	# 	if self.id:
	# 		return str(self.id)
	# 	else:
	# 		super(Screen, self).save(*args, **kwargs)

	def get_absolute_url(self):
			return reverse('screen_detail', kwargs={'pk': self.pk})

	def __str__(self):
		header = 'Screen-'
		myid = str(self.id)
		if self.id < 10:
			header = 'Screen-0'
		list = [header, myid]
		return ''.join(list)

	class Meta:
		ordering = ('location',)

class MediaType(models.Model):
	URL_LINK = 1
	VIDEO_LINK = 2
	PIC_LINK = 3
	TYPE_CHOICES = (
			(URL_LINK, 'url'),
			(VIDEO_LINK, 'video'),
			(PIC_LINK, 'pic'),
			)
	type_name = models.IntegerField(choices = TYPE_CHOICES)

	def __str__(self):
		ind = self.type_name -1
		return str(self.TYPE_CHOICES[ind])


class Category(models.Model):
	category_name = models.CharField(max_length = 30)

	def __str__(self):
		return self.category_name


class Link(models.Model):
	url = models.URLField(max_length = 200, unique = True)
	link_type = models.ForeignKey(MediaType, on_delete = models.CASCADE)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	readonly_fields = ('url',)


	def get_absolute_url(self):
        	return reverse('link_detail', kwargs={'pk': self.pk})

	def __str__(self):
		return self.url

	class Meta:
		ordering = ('url',)


class ScreenLink(models.Model):
	sl_screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
	sl_link = models.ForeignKey(Link, on_delete = models.CASCADE)
	display_time = models.PositiveIntegerField(default = 60)
	position = models.PositiveIntegerField(default = 1)


	def get_absolute_url(self):
        	return reverse('sl_detail', kwargs={'pk': self.pk})
	def __str__(self):
		return self.sl_link.url
	class Meta:
		ordering = ('position', )
