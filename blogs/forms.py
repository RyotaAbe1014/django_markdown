from mdeditor.fields import MDTextFormField # 追加
from django  import forms


class ArticleForm (forms.Form):
    title = forms.CharField()
    content = MDTextFormField()
