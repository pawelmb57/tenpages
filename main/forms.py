from django import forms
from .models import Books, UserBooks, LogPages


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
    class Meta:
        model = LogPages
        fields = ('log_pages','userbooks')

    def __init__(self, user, *args, **kwargs):
        super(LogPagesForm, self).__init__(*args, **kwargs)
        self.fields['userbooks'].queryset = UserBooks.objects.filter(user=user)
