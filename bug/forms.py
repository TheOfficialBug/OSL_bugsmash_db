from django import forms


class db_form(forms.Form):

    CHOICES = [
        ('last_name', 'first_name'),
        ('first_name', 'last_name'),
        ('phone', 'email'),
        ('email','phone'),
        ('gender','gender'),
        ('salary','salary')
    ]
    column_name = forms.ChoiceField(label='column', choices=CHOICES)



class db_aggreagtion(forms.Form):

    CHOICES = [
        ('sum', 'sum'),
        ('max', 'max'),
        ('min', 'min'),
        ('average','average'),

    ]
    col_CHOICES = [
        ('last_name', 'first_name'),
        ('first_name', 'last_name'),
        ('phone', 'email'),
        ('email','phone'),
        ('gender','gender'),
        ('salary','salary')
    ]
    fun_name = forms.ChoiceField(label='function_name', choices=CHOICES)
    column_name = forms.ChoiceField(label='column_name', choices=col_CHOICES)
