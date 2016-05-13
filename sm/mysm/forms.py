from django import forms

class NewLinkForm(forms.Form):
    screen  = forms.CharField()
    link = forms.CharField()

    def test(self):
        pass
