from django.shortcuts import render
import jdatetime
from django import forms

class BirthdayForm(forms.Form):
    year = forms.IntegerField(label='Birth Year',widget= forms.TextInput(attrs={'placeholder':'e.g. 1382'}))
    month = forms.IntegerField(label='Birth Month',widget= forms.TextInput(attrs={'placeholder':'e.g. 8'}))
    day = forms.IntegerField(label='Birth Day',widget= forms.TextInput(attrs={'placeholder':'e.g. 7'}))

# Create your views here.
now_year = jdatetime.datetime.now().year
now_month = jdatetime.datetime.now().month
now_day = jdatetime.datetime.now().day


def index(request):
    if request.method == 'POST':
        form = BirthdayForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            month = form.cleaned_data['month']
            day = form.cleaned_data['day']

            total_age = ((now_year-(year+1))*365.25 + 30.5*(12 - abs(month-now_month)) + abs(day-now_day) + 1)/365.25
            age = round(total_age, 1)


            return render(request, 'birthcertificate/result.html', {
                'Sun': 0,
                "Mercury" : round(age*365.25/88,1),
                "Venus" : round(age*365.25/225,1),
                'Earth': age,
                "Mars" : round(age*365.25/(365.25+321.73),1),
                "Jupiter" : round(age*365.25/(11*365.25+313.839),1),
                "Satturn" : round(age*365.25/(29*365.25+167),1),
                "Uranus" : round(age*365.25/(84*365.25+4),1),
                "Neptun" : round(age*365.25/(164*365.25+288),1),
                "Pluto" : round(age*365.25/(247*365.25+248),1)
                })
    else:
        form = BirthdayForm()
    return render(request, 'birthcertificate/index.html', {'form': form})