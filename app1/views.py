from django.shortcuts import render
from .models import *
from django.http import JsonResponse
# Create your views here.

def index(request):
    countries = Countries.objects.all()
    all_u = User.objects.all()
    return render(request, 'index.html', {'all_countries': countries, 'all_data': all_u })

def get_cities(request):
    cid = request.GET['country_id']
    co_obj = Countries.objects.get(id = cid)
    filtered_cities = list(Cities.objects.filter(country = co_obj).values())
    return JsonResponse({'all_cities': filtered_cities})


def row_create(request):
    co_obj = Countries.objects.get(country_name = request.POST['country'])
    User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        city = Cities.objects.get(country = co_obj, city_name = request.POST['city'])
    )
    all_data = list(User.objects.all().values())
    for idx in range(len(all_data)):
        
        ci_obj = Cities.objects.get(id = all_data[idx]['city_id'])
        all_data[idx]['city_name'] = ci_obj.city_name
        all_data[idx]['country_name'] = ci_obj.country.country_name

    return JsonResponse({'updated_data': all_data})
"""
[{'id': 1, 'first_name': 'Mit', 'last_name': 'Desai', 'city_id': 10}, 
 {'id': 2, 'first_name': 'Divyesh', 'last_name': 'Sony', 'city_id': 1}, {'id': 3, 'first_name': 'Murari', 'last_name': 'Jha', 'city_id': 2}, 
 {'id': 4, 'first_name': 'Avinash', 'last_name': 'Patil', 'city_id': 8}, 
 {'id': 5, 'first_name': 'Avi', 'last_name': 'Pa', 'city_id': 7}]
"""