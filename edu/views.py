from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import View, DetailView
from .models import Feed 
# Create your views here.
class Index(View):
    template_name= 'index.html'

    def get(self, request):
        return render(request, self.template_name)      

class TagStudy(View):
    template_name= 'tag_study.html'

    def get(self, request):
        feeds = Feed.objects.all().order_by('id')
        print(f"feed size:{len(feeds)}")
        return render(
        request,
        self.template_name,
            {'feed_list':feeds}
                )    
     
class NewContent(View):
    template_name= 'upload_form.html'    

    def get(self, request):
        return render(request, self.template_name)
    
        

    def post(self, request):
        age = request.POST.get('age','0')
        age = int(age)
        print(f'age:{age}')
        
        
        pwd = request.POST.get('pwd','0')
        print(f'비밀번호:{pwd}')

        tel = request.POST.get('phone','0')
        print(f'전화번호:{tel}')
        search = request.POST.get('sch','0')
        print(f'전화번호:{search}')

        param = request.POST.get('content','')
        param2= request.FILES.get('up_photo', False)
        print(param)
        feed = Feed(content = param , photo = param2)
        feed.save()
        return redirect('edu:tag_study')
class Subway(View):
    template_name= 'subway.html'

    def get(self, request):
        return render(request, self.template_name)
class FeedDetail(DetailView):
    model = Feed
    template_name ="feed/detail.html"
    def get_context_data(self,**kwargs) :
        context = super().get_context_data(**kwargs)
        feed = get_object_or_404(Feed, pk = self.kwargs['pk'])
        context['feed'] = feed
        return context
