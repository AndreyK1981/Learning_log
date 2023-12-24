from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}  # Почему Entry: не отображается ?
        widgets = {'text':  forms.Textarea(attrs={'rows': 10, 'cols': 80})}
        # widgets = {'text': forms.Textarea(attrs={"style": "height:60px; width:500px"})}
        # long_desc = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 20}))