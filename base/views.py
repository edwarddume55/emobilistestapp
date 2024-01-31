from django.shortcuts import redirect, render
from .models import Message
from .forms import MessageForm
# Create your views here.


def inbox(request):
    inbox= Message.objects.all().order_by('is_read')
    unreadCount=Message.objects.filter(is_read=False).count()
    context={'inbox':inbox, 'unreadCount':unreadCount,}
    return render(request, 'index.html',context)


def sendMessage(request):
    form=MessageForm()

    if request.method == 'POST':
        form=MessageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    context={'form':form}
    return render(request, 'message.html',context)


def editMessage(request,pk):
    project=Message.objects.get(id=pk)
    form=MessageForm(instance=project)

    if request.method == 'POST':
        form=MessageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request, 'Message.html',context)


def destroy(request, id):
    Message = Message.objects.get(id=id)
    Message.delete()
    return redirect(request, 'Message.html')