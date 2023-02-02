from django.shortcuts import render, redirect
from .models import Topic, Choice
from django.contrib import messages
from django.contrib import messages

# Create your views here.
def index(request):
    t = Topic.objects.all()
    ct = {
        "tset" : t,
    }
    return render(request, "vote/index.html", ct)

def detail(request, tpk):
    t = Topic.objects.get(id=tpk)
    c = t.choice_set.all()
    ct = {
        "t" : t,
        "cset" : c,
    }

    return render(request,"vote/detail.html", ct)


def vote(request, tpk):
    t = Topic.objects.get(id=tpk)
    if not request.user in t.voter.all():
        t.voter.add(request.user)
        cpk = request.POST.get("cho")
        c = Choice.objects.get(id=cpk)
        c.choicer.add(request.user)

    return redirect("vote:detail", tpk)

def cancle(requset, tpk):
    u = requset.user
    t = Topic.objects.get(id=tpk)
    u.choice_set.get(top=t).choicer.remove(u)
    t.voter.remove(u)
    return redirect("vote:detail", tpk)    

def delete(request, tpk):
    t = Topic.objects.get(id=tpk)
    c = t.choice_set.all()
    if request.user == t.maker:
        t.delete()
    else:
        messages.error(request, "본인이 작성한 투표만 삭제할 수 있습니다.")
    return redirect("vote:index")

def create(request):
    if request.method == "POST":
        s = request.POST.get("sub")
        c = request.POST.get("con")
        cn = request.POST.getlist("cname")
        cc = request.POST.getlist("ccon")
        t = Topic(subject=s, content=c, maker=request.user)
        t.save()
        for name, com in zip(cn, cc):
            c = Choice(top=t, name=name, comment=com).save()
        messages.info(request, "토픽 생성 완료!")
        return redirect("vote:index")

    return render(request, "vote/create.html")