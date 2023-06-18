from django import forms
from django.core.exceptions import ValidationError

class Update_dB_form(forms.Form):
    f_Author= forms.CharField(label="Author",max_length=50,)
    f_Author_email_add= forms.EmailField(label="Email_id")
    f_Book_Title= forms.CharField(label="Title",max_length=50,)
    f_Book_Publisher_Name = forms.CharField(label="Publisher",max_length="50",)
    f_Publication_Date= forms.DecimalField(label="Production Year",max_digits=4)
    f_Issue_State= forms.BooleanField(label="Issue Status",required=False)
    f_Issue_Roll_No= forms.DecimalField(label="Issued Roll No",max_digits=5,required=False)