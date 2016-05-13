from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from mysm.models import Screen, Link, ScreenLink

from django.core.urlresolvers import reverse_lazy

# Create your views here.

from django.http import HttpResponse

def index(request):
	    return HttpResponse("Rango says hey there world!")
#************Screen Views
class ScreenList(ListView):
	model = Screen

class ScreenCreate(CreateView):
    model = Screen
    fields = ['brand','model','location']

class ScreenDetail(DetailView):
	model = Screen

	def get_context_data(self, **kwargs):
		context = super(ScreenDetail, self).get_context_data(**kwargs)
		urls_screen = ScreenLink.objects.filter(sl_screen = self.kwargs['pk'])
		dLinks = []
		dTimes = []
		dsl = []


		for i in urls_screen:
			dTimes.append(i.display_time)
			a = Link.objects.get(url=i)
			dLinks.append(a)
			b = i.id
			dsl.append(b)

		context['myscreen'] = Screen.objects.get(id = self.kwargs['pk'])
		context['mysl'] = urls_screen
		context['links'] = zip(dLinks,dTimes,dsl)

		return context

class ScreenUpdate(UpdateView):
    model = Screen
    fields = ['location', 'brand', 'model']
    template_name_suffix = '_update_form'

class ScreenDelete(DeleteView):
    model = Screen
    success_url = reverse_lazy('screen_list')
#************Link Views
class LinkCreate(CreateView):
    model = Link
    fields = ['url','category','link_type']

class LinkDetail(DetailView):
	model = Link

class LinkList(ListView):
	model = Link

class LinkDelete(DeleteView):
    model = Link
    success_url = reverse_lazy('link_list')

class LinkUpdate(UpdateView):
	model = Link
	fields = ['url', 'link_type', 'category']
	template_name_suffix = '_update_form'
#************ScreenLink Views
class ScreenLinkList(ListView):
	model = ScreenLink

class ScreenLinkCreate(CreateView):
	model = ScreenLink
	fields = ['sl_screen', 'sl_link', 'display_time']

class ScreenLinkCreateScreen(CreateView):
	model = ScreenLink
	fields = ['sl_link', 'display_time']
	template_name_suffix = '_create_cat'

    	def get_context_data(self, **kwargs):
			context = super(ScreenLinkCreateScreen, self).get_context_data(**kwargs)
			context['readers'] = self.kwargs['pk']
			return context


class ScreenLinkDetail(DetailView):
	model = ScreenLink

class ScreenLinkDelete(DeleteView):
    model = ScreenLink
    success_url = reverse_lazy('sl_list')

class ScreenLinkUpdate(UpdateView):
	model = ScreenLink
	fields = ['sl_screen', 'sl_link', 'display_time']
	template_name_suffix = '_update_form'
#********************************************
from django.views.generic.base import TemplateView
class myView(TemplateView):
	template_name = "myview.html"

	def get_context_data(self, **kwargs):
		context =super(myView, self).get_context_data(**kwargs)
		context['mydata'] = ScreenLink
#********************************************

from mysm.forms import NewLinkForm
from django.views.generic.edit import FormView

class NewLink(FormView):
	template_name = 'newlink.html'
	form_class = NewLinkForm
	success_url = '/sl/'

	def form_valid(self, form):
		form.test()
		return super(NewLink, self).form_valid(form)

from django.http import JsonResponse

def getObject(request, id):
	objList = ScreenLink.objects.filter(sl_screen = id).values('position', 'display_time', 'sl_link__url')

	return JsonResponse({'links':list(objList)})
