from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect

class oneNameMapForm(forms.Form):
    search_fname = forms.CharField(label='Name:', max_length=30)
    search_year1 = forms.CharField(label='Starting year:', max_length=4)
    search_year2 = forms.CharField(label='Ending year:', max_length=4)
    search_animate_choice = forms.ChoiceField(label='', widget=forms.RadioSelect, choices=[('separate','separate maps'),('animated','animated map')])
    search_sexFM = forms.CharField(label='Sex (F/M):', max_length=1)
    # dummy = forms.CharField(label='DUMMY', widget=forms.HiddenInput(), max_length=10, initial="dummy")

    # let's validate the sex field...
    def clean_sexFM(self):
        data = self.cleaned_data['search_sexFM']
        if data == "A":
            raise ValidationError(_('Invalid sex; must be F or M'))
        return data

    def __init__(self, *args, **kwargs):
        super(oneNameMapForm, self).__init__(*args, **kwargs)
        self.fields['search_year1'].required = False
        self.fields['search_year2'].required = False
        self.fields['search_sexFM'].required = False

class oneStateNameReportForm(forms.Form):
    search_state = forms.CharField(label='State:', max_length=2)
    search_year1 = forms.CharField(label='Year:', max_length=4)

class oneYearHundredNamesMapForm(forms.Form):
    search_year1 = forms.CharField(label='Year:', max_length=4)
    search_sexFM = forms.CharField(label='Sex:', max_length=1)
    search_number_limit = forms.CharField(label='Number of names to use:', max_length=3)

    def __init__(self, *args, **kwargs):
        super(oneYearHundredNamesMapForm, self).__init__(*args, **kwargs)
        self.fields['search_sexFM'].required = False
        self.fields['search_number_limit'].required = False

class oneYearAllStatesComparisonReportForm(forms.Form):
    search_year1 = forms.CharField(label='Year:', max_length=4)
    search_number_limit = forms.CharField(label='Number of names to use:', max_length=3)

    def __init__(self, *args, **kwargs):
        super(oneYearAllStatesComparisonReportForm, self).__init__(*args, **kwargs)
        self.fields['search_number_limit'].required = False

class allStatesToOneStateMapForm(forms.Form):
    search_state = forms.CharField(label='State:', max_length=2)
    search_year1 = forms.CharField(label='Year:', max_length=4)
    search_number_limit = forms.CharField(label='Number of names to use:', max_length=3)

    def __init__(self, *args, **kwargs):
        super(allStatesToOneStateMapForm, self).__init__(*args, **kwargs)
        self.fields['search_number_limit'].required = False
