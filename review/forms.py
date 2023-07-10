from django import forms
from .models import Review, Comments

class DateInput(forms.DateInput):
    input_type = 'date'

class ReviewForm(forms.ModelForm):
    watched_date = forms.DateField(label='언제 감상하셨나요?', widget=DateInput)
    content = forms.CharField(label='간단히 기록하기:', widget=forms.Textarea(attrs={'cols': '40', 'rows': '5'}))

    class Meta:
        model = Review
        fields = ['content']

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['re_comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["re_comment"].label = "댓글"
        self.fields["re_comment"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "댓글을 입력하세요."
        })

