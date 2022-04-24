from django.shortcuts import render

# Create your views here.

from json import dumps
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader

from .forms import InputForm
import googlemaps

from django.confg.settings import gmap_API_KEY

gmaps = googlemaps.Client(key= gmap_API_KEY )



def input_view(request):
    context ={}
    context['form']= InputForm()
    
    return render(request,'home.html',context)



def result_view(request):#/getAddressDetails
    
    
    context =  {}
    if request.method == 'POST':
        form = InputForm(request.POST)

        if form.is_valid():
            address = form.cleaned_data.get('address')
            out_format = form.cleaned_data.get('output_format')
            print('address:', address  )
            print('format:', out_format )

    geocode_result = gmaps.geocode(address)
    out = geocode_result[0]['geometry']['location']
    
    d = {"coordinates":out,"addresss":address}
    

   
    json_string = dumps(d)
    if out_format == "JSON":
        return JsonResponse(d)
    elif out_format == "XML":
#        response = render_to_response('xml_result.xml', {'address': address, 'out' : out})
#        response['Content-Type'] = 'application/xml;'
#        return response
        t = loader.get_template('xml_result.xml')
        return HttpResponse(t.render({'address': address, 'out' : out}, request), content_type='application/xml')
    
    return render(request,'result.html',{"data" :json_string})





    