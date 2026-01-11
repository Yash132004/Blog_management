from django.shortcuts import get_object_or_404,render
from blog.models import Blog

# Create your views here.
def blogDetail(request,pk):
    blog = get_object_or_404(Blog, pk=pk )
    context = {'blog':blog}
    return render(request, 'blogDetail.html',context)