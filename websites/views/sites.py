from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone

#Mixin Auth system
from django.contrib.auth.mixins import LoginRequiredMixin
#Decorators
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

#CBV
from django.views.generic import (
    ListView,
    DetailView,
    FormView
)

from websites.tools import checking

from websites.models.website import Website
from websites.forms.website import WebsitesForm

class ListWebsiteView(ListView):
    template_name = 'websites/list.html'
    context_object_name = 'websites_list'

    def get_queryset(self):
        return Website.objects.all()

class WebsiteDetailView(DetailView):
    model = Website
    template_name = 'websites/detail.html'

    def get_context_data(self, **kwargs):
        #Get context
        context = super().get_context_data(**kwargs)
        #Get object value just for return some info about details
        website_obj = context.get('object', None)
        from_class = WebsitesForm(instance=website_obj)
        context['form'] = from_class

        return context
    
class WebsiteDNSView(DetailView):
    model = Website
    template_name = 'websites/dns.html'

    def get_context_data(self, **kwargs):
        #Get context
        context = super().get_context_data(**kwargs)
        #Get object value just for return some info about details
        website_obj = context.get('object', None)

        #value for domain info
        if website_obj:
            #HTTP STATUS CODE
            code_status = checking.website_code_status(website_obj.formated_domain)
            context['codestatus'] = f'{code_status[0]} - {code_status[1]}' if code_status else False
            
            #DNS RECORDS INFO, JUST A, TXT AND NS values
            dns_records = checking.dns_resolver(website_obj.domain, ['A', 'TXT', 'NS']) #<- dns_resolver required a list of records in this case those 3.
            context['a_records'] = dns_records.get('A', None)
            context['txt_records'] = dns_records.get('TXT', None)
            context['ns_records'] = dns_records.get('NS', None)

            #IMAGE CAPTION
            data = checking.imgs_caption(website_obj.formated_domain)
            #probably this value will get you more than you expect (Basically for SEO shits about imgs or others imgs related in the home page)
            if data and len(data) > 2:
                #This condicional will try it to get the frist value of the home page, hoping the first value is the Logo and the caption if have it
                #Try to get the first position of the list to reduce the posibilities of missing any info.
                #And then the first position of the list, this probably will get you the correct list value.
                data_set_img = str(data[0][0]) #<- First position of the big list and then second list reduced - will get you img data
                data_set_caption = data[0][1] #<-  First position of the big list and then second list reduced - will get you caption data in bytes
                
                #Try to edit the current str value adding tha class for bootstrap
                if 'data-lazy-src' in data_set_img:
                    context['data_img'] = checking.parsing_img(data_set_img) #BEWARE WITH THIS
                else:
                    context['data_img'] = data_set_img[:4]+' class="card-img-top mt-2"'+data_set_img[4:] #BEWARE WITH THIS

                context['data_caption'] = data_set_caption.decode() if data_set_caption.decode() != '' else 'No Caption Available'

        return context

class WebsiteCustomFormView(FormView):

    def post(self, request, *args, **kwargs):
        website_obj = get_object_or_404(
            Website,
            id=request.POST.get('wbid')
            )
        form = WebsitesForm(request.POST, instance=website_obj)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('websites:website_control_detail', args=[request.POST.get('wbid')]))

