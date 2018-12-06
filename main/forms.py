from django import forms
from .models import Books, UserBooks, LogPages
import datetime

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ('book_title', 'book_total_pages')
        # book_title =        forms.CharField(max_length=100)
        # book_total_pages =  forms.IntegerField()

class AddBookUserForm(forms.ModelForm):
    class Meta:
        model = UserBooks
        fields = ('user',)

class LogPagesForm(forms.ModelForm):

    # log_date = forms.DateField(
    #     widget = forms.DateInput(format=('%m/%d/%Y'),
    #                             attrs={'class': 'form-control',
    #                                    'type': 'date',
    #                                    'label': '01/01/2018'})
    # )

    class Meta:
        model = LogPages
        fields = ('log_pages','userbooks','log_date')

        # widgets = {
        #     'log_date': forms.DateInput(format=('%m/%d/%Y'), attrs={}),
        #     }

    def __init__(self, user, *args, **kwargs):
        super(LogPagesForm, self).__init__(*args, **kwargs)
        self.fields['userbooks'].queryset = UserBooks.objects.filter(user=user)
        self.fields['log_date'].initial = datetime.date.today().strftime('%Y-%m-%d')
