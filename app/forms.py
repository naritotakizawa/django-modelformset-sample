from django import forms
from .models import Post


class PostCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Post
        fields = '__all__'


# これがモデルフォームセット
PostCreateFormSet = forms.modelformset_factory(
    Post, form=PostCreateForm, extra=3
)
