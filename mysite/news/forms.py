from django import forms
from .models import Category, News, Feedback


# # связ с формами
# class FeedbackForm(forms.ModelForm):
#     class Meta:
#         model = Feedback
#         fields = ['name', 'contact', 'message']
#         widgets = {
#             'name': forms.TextInput(attrs={"class": "form-control"}),
#             'contact': forms.TextInput(attrs={"class": "form-control"}),
#             'message': forms.Textarea(attrs={"class": "form-control", "rows": 5})
#         }


# не связ с формами
class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class": "form-control"}),
                           label="Как вас зовут:")
    contact = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class": "form-control"}),
                              label="Ваши контактные данные, если хотите чтоб мы с вами связались:")
    message = forms.CharField(required=False,
                              widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}),
                              label="Ваш отзыв:")


# связ с формами
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'category': forms.Select(attrs={"class": "form-control"})
        }

# не связ с формами
# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class": "form-control"}),
#                             label="Заголовок:")
#     content = forms.CharField(required=False,
#                               widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}),
#                               label="Содержание:")
#     is_published = forms.BooleanField(initial=True,
#                                       label="Опубликовано:")
#     category = forms.ModelChoiceField(empty_label="Выберите категорию", queryset=Category.objects.all(),
#                                       widget=forms.Select(attrs={"class": "form-control"}),
#                                       label="Категория:")
