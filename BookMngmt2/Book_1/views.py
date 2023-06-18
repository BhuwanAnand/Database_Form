# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . form import Update_dB_form
from . models import Book

def Search(request):
    blank_form = Update_dB_form(request.POST or None)
    if request.method == 'POST':
        if blank_form.is_valid():
            Author_N = blank_form.cleaned_data.get("f_Author")
            email = blank_form.cleaned_data.get("f_Author_email_add")
            B_Title = blank_form.cleaned_data.get("f_Book_Title")
            B_Pub_Name = blank_form.cleaned_data.get("f_Book_Publisher_Name")
            B_Pub_Date = blank_form.cleaned_data.get("f_Publication_Date")
            B_Issu_Stat = blank_form.cleaned_data.get("f_Issue_State")
            B_Roll = blank_form.cleaned_data.get("f_Issue_Roll_No")

            p2 = Book(
                auth_first_name=Author_N,
                auth_email=email,
                Title=B_Title,
                Publisher=B_Pub_Name,
                Publication_year=B_Pub_Date,
                Issue_status=B_Issu_Stat,
                Issued_roll_no=B_Roll,
            )
            p2.save()

            detail_list = Book.objects.all()
            return render(request, "Update.html", {"blank_form": blank_form})
    else:
        blank_form = Update_dB_form()

    return render(request, "Update.html", {"blank_form": blank_form})
