from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone

from django.views.generic import (
    ListView,
    DetailView,
    FormView
)

from websites.models.website import Website
from django.db.models import Q

from websites.tools import checking

class IndexListWebsiteView(ListView):
    template_name = 'home/index.html'
    context_object_name = 'websites_list'

    def get_queryset(self): 
        """Return the last five published questions (not including those set to be published in the future)."""
        # return Question.objects.order_by('-pub_date')[:5]
        #return Website.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
        return Website.objects.all()

class IndexWebsiteStatusView(DetailView):
    model = Website
    template_name = 'home/status.html'

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

class IndexSearchWebsites(ListView):
    template_name = 'home/index.html'
    context_object_name = 'websites_list'
    
    def get_queryset(self):
        filters = Q(domain__icontains=self.query())
        return Website.objects.filter(filters) 

    def query(self):
        return self.request.GET.get('searchhome')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        return context

class IndexWebsiteDetailView(DetailView):
    model = Website
    template_name = 'home/detail.html'
