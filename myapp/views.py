from django.shortcuts import render
import requests
from PIL import Image
from ast import literal_eval
import json
from django.http import JsonResponse
from . models import RegisteredClient

# Create your views here.
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
LANGUAGE = "en-US,en;q=0.5"
session = requests.Session()
session.headers['User-Agent'] = USER_AGENT
session.headers['Accept-Language'] = LANGUAGE
session.headers['Content-Language'] = LANGUAGE
session.headers['Origin'] = 'https://electoralsearch.in'
session.headers['Referer'] = 'https://electoralsearch.in/'


def index(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        state = request.POST.get('state')
        district = request.POST.get('district')
        ac = request.POST.get('AC')
        fname = request.POST.get('fname')
        gender = request.POST.get('gender')
        payload = {
            "txtCaptcha":request.POST.get('captcha'),
            "search_type":"details",
            "reureureired":"ca3ac2c8-4676-48eb-9129-4cdce3adf6ea",
            "name":name,
            "rln_name":fname,
            "page_no":1,
            "location":f"{state},{district},{ac}",
            "results_per_page":10,
            "location_range":"20",
            "age":age,
            "dob":None,
            "gender":gender
            }
        
        results = session.post("https://electoralsearch.in/Home/searchVoter",json=payload)
        results = results.text
        
        json_result = json.loads(results)
        final_dict = json_result['response']['docs'][0]
        epic_no = final_dict['epic_no']
        st_name = final_dict['st_name']
        st_code = final_dict['st_code']
        dist_name = final_dict['dist_name']
        dist_no = final_dict['dist_no']
        ac_name = final_dict['ac_name']
        ac_no = final_dict['ac_no']
        part_name = final_dict['part_name']
        part_no = final_dict['part_name']
        name = final_dict['name']
        age = final_dict['age']
        gender = final_dict['gender']
        rln_name = final_dict['rln_name']
        rln_type = final_dict['rln_type']

        return JsonResponse(final_dict)

    results = session.get("https://electoralsearch.in/Home/GetCaptcha?image=true")
    file = open('test.jfif','wb')
    file.write(results.content)
    file.close()

    im = Image.open('test.jfif')
    im.save('static/captcha.jpeg')            
    state_list = session.get('https://electoralsearch.in/Home/GetStateList')
    state_list = state_list.content
    state_list = literal_eval(state_list.decode('utf-8'))

        

    
    return render(request,'index.html',{'states' : state_list,})

def load_districts(request):
    global state_code
    state_code = request.GET.get('state_id')

    district_url = f"https://electoralsearch.in/Home/GetDistList?st_code={state_code}"
    district_list = session.get(district_url)
    district_list = district_list.content
    district_list = literal_eval(district_list.decode('utf-8'))

    return render(request,'district_dropdown.html',{'districts' : district_list})

def load_acs(request):
    district_code = request.GET.get('district_id')
    print(district_code,state_code)
    acs_url = f"https://electoralsearch.in/Home/GetAcList?dist_no={district_code}&st_code={state_code}"
    acs_list = session.get(acs_url)
    acs_list = acs_list.content
    acs_list = literal_eval(acs_list.decode('utf-8'))
    
    return render(request,'acs_dropdown.html',{'ACs' : acs_list})

   