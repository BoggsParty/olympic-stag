from django.forms import ModelForm
from django import forms
from sports.models import Athlete, Sport
from .models import Guesses, Comments, Responses

class GuessForm(ModelForm):

    class Meta:
        model = Guesses
        fields = ('gold','silver','bronze',)
    def __init__(self, *args, **kwargs):
        sport = kwargs.pop('sport')
        sport_query = Sport.objects.get(slug=sport)
        sport_id = sport_query.id
        super(GuessForm, self).__init__(*args, **kwargs)
        self.fields['gold'].queryset = self.fields['gold'].queryset.filter(sports=sport_id)
        self.fields['silver'].queryset = self.fields['silver'].queryset.filter(sports=sport_id)
        self.fields['bronze'].queryset = self.fields['bronze'].queryset.filter(sports=sport_id)


class NewCommentForm(ModelForm):
    
    class Meta:
        model = Comments
        fields = ('message',)
        
class NewResponseForm(ModelForm):
    
    class Meta:
        model = Responses
        fields = ('message',)
    