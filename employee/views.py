from django.shortcuts import get_object_or_404,render
from employee.models import Employee

# Create your views here.
def employeeDetail(request,pk):
    employee = get_object_or_404(Employee, pk=pk )
    context = {'employee':employee}
    return render(request, 'employeeDetail.html',context)