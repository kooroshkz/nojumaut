from django.shortcuts import render
import jdatetime
from django import forms

class BirthdayForm(forms.Form):
    year = forms.IntegerField(label='Birth Year')
    month = forms.IntegerField(label='Birth Month')
    day = forms.IntegerField(label='Birth Day')

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


            return render(request, 'result.html', {'age': age})
    else:
        form = BirthdayForm()
    return render(request, 'birthcertificate/index.html', {'form': form})