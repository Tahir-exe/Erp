from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Employee

from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import permission_required

from django.shortcuts import redirect
from .forms import EmployeeForm

def index(request):
    return render(request, "erp/index.html")

@permission_required("erp.can_view_employee", raise_exception=True)
@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "erp/employee_list.html", {"employees": employees})


@permission_required("erp.can_add_employee", raise_exception=True)
@login_required
def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = EmployeeForm()
    return render(request, "erp/add_employee.html", {"form": form})
from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm  # Assuming you have a form for adding employees
