from django.http import HttpResponse , FileResponse , JsonResponse
from django.shortcuts import render
def waht_is_my_ip (requset):


    return JsonResponse({'ip':'1234567890'})



def home(request):
   return render( request , 'myapp/home.html' ,{} )




#def home(requset):         #www.Nani.com/home
    #return FileResponse(open('myapp/song.mp3' , 'rb'))



#def about(requset):
   # return HttpResponse('<h1>About Page</h1>')


#def contact(requset):
  #return HttpResponse('<P>hello world iam Naema</p>')
   
