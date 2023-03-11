from django.shortcuts import render,get_object_or_404
from .models import  PollingUnit,AnnouncedPuResult , Lga
from django.db.models import Sum
def polling_unit_result(request, uniqueid):
    try:
        polling_unit = get_object_or_404(PollingUnit, uniqueid=uniqueid)
    except PollingUnit.DoesNotExist:
        return render(request, 'polling_unit_error.html', {'uniqueid': uniqueid})

    announced_results = AnnouncedPuResult.objects.filter(polling_unit_uniqueid=uniqueid)

    results = {}
    for result in announced_results:
        results[result.party_abbreviation] = result.party_score

    return render(request, 'polling_unit_result.html', {'polling_unit': polling_unit, 'results': results})


def lga_polling_unit_results(request):
    if request.method == 'POST':
        lga_id = request.POST.get('lga')
        polling_units = PollingUnit.objects.filter(lga_id=lga_id)
        print('polling_units', polling_units)
        total_results = {}
        resulting= {}
        for pu in polling_units:
            results = AnnouncedPuResult.objects.filter(polling_unit_uniqueid=pu.uniqueid)
            print(pu)
            for result in results:
                if result.party_abbreviation in total_results:
                    total_results[result.party_abbreviation] += result.party_score
                else:
                    total_results[result.party_abbreviation] = result.party_score
        return render(request, 'lga_polling_unit_results.html', {'total_results': total_results,'results':resulting,'polling_units':polling_units})
    else:
        return render(request, 'lga_polling_unit.html')

def select_lga(request):
    lgas = Lga.objects.all()
    return render(request, 'select_lga.html', {'lgas': lgas})



def new_polling_unit_result(request):
    if request.method == 'POST':
        # Get the selected polling unit
        uniqueid = request.POST.get('polling_unit')
        polling_unit = get_object_or_404(PollingUnit, uniqueid=uniqueid)
        # Save the results for each party
        parties = ['party1', 'party2', 'party3']
        for party in parties:
            party_score = request.POST.get(party)
            result = AnnouncedPuResult(polling_unit_uniqueid=polling_unit.uniqueid, party_abbreviation=party, party_score=party_score)
            result.save()
        # Return a success message
        return render(request, 'new_polling_unit_result_success.html')
    else:
        # Render the form
        polling_units = PollingUnit.objects.all()
        return render(request, 'new_polling_unit_result.html', {'polling_units': polling_units})