from django.http import JsonResponse
from myapp.models import ElectoralDataTable
import json


def api_home(request, *args, **kwargs):
    try:
        body = request.body

        data = {}
        output = {}
        try:
            data = json.loads(body)
        except:
            pass
        print(data)
        user = ElectoralDataTable.objects.get(epic_no=data['epic_no'])
    
        residents = ElectoralDataTable.objects.all()
        i = 1
        for resident in residents:
            if resident.house_no == user.house_no:
            
                output[f'{i}'] = {'name': resident.name,"father's Name" : resident.fname,"Age":resident.age,"Gender" : resident.gender,"VoterID Number" : resident.epic_no}
                i = i+1
                print(resident.name)

    except Exception as e :
        output = {"Result":"Failed"}
    return JsonResponse(output)