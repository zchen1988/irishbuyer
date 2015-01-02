from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from IrishFashionBuyer.models import Order,OrderDetails
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from IrishFashionBuyer.forms import OrderForm
from django.utils import timezone


# Create your views here.
def index(request):
    latest_order = Order.objects.all()
    context = {'latest_order':latest_order}
    return render(request,'IrishFashionBuyer/index.html',context)

# Create your views here.
def details(request,order_number):
    details = OrderDetails.objects.filter(order_number=order_number)
    order = Order.objects.filter(order_number=order_number)
    context = {'details':details,'order':order}
    return render(request,'IrishFashionBuyer/details.html',context)

def agentlogin(request):
    return render(request,'IrishFashionBuyer/agentlogin.html')

def auth_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            if user.is_superuser:
                return HttpResponseRedirect(reverse('fashion:admin_order'))
            else:
                return HttpResponseRedirect(reverse('fashion:agent_order'))
        else:
            print("not active")
    else:
        print("failed")

def agent_order(request):
    agent = request.user
    if not request.user.is_authenticated():
        return render(request,'IrishFashionBuyer/agentorderpage.html')

    orders = Order.objects.filter(order_user=request.user)
    orderlist = []
    for order in orders:
        orderdetails = OrderDetails.objects.filter(order_number=order.order_number)
        order_dic = {'order_number':order.order_number,'date':order.order_time,'delivery_number':order.delivery_number,'address':order.delivery_address,'items':'','price':order.total_price,'paid':order.order_paid,'comments':order.order_comments}
        items = ''
        for orderdetail in orderdetails:
            items = items + orderdetail.product_name+'*'+str(orderdetail.product_quantity)+'*'+str(orderdetail.product_price)+', '
        order_dic['items'] = items
        orderlist.append(order_dic)

    context = {'agent':agent,'orderlist':orderlist}
    return render(request,'IrishFashionBuyer/agentorderpage.html',context)

def admin_order(request):
    admin = request.user
    if not request.user.is_authenticated():
        return render(request,'IrishFashionBuyer/agentorderpage.html')
    orders = Order.objects.all()
    orderlist = []
    for order in orders:
        orderdetails = OrderDetails.objects.filter(order_number=order.order_number)
        order_dic = {'order_number':order.order_number,'date':order.order_time,'delivery_number':order.delivery_number,'address':order.delivery_address,'items':'','price':order.total_price,'paid':order.order_paid,'comments':order.order_comments}
        items = ''
        for orderdetail in orderdetails:
            items = items + orderdetail.product_name+'*'+str(orderdetail.product_quantity)+'*'+str(orderdetail.product_price)+', '
        order_dic['items'] = items
        orderlist.append(order_dic)

    context = {'admin':admin,'orderlist':orderlist}
    return render(request,'IrishFashionBuyer/adminorderpage.html',context)



def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('fashion:agentlogin'))


def add(request,order_number):
    order = Order.objects.filter(order_number=order_number)
    return HttpResponseRedirect(reverse('fashion:details',args=(order.get().order_number,)))

def add_new_order(request):

    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('fashion:agentlogin'))

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            totalPrice = request.POST.get('total_price')
            address = request.POST.get('delivery_address')
            comments = request.POST.get('comments')
            if request.POST.get('order_paid'):
                paid = request.POST.get('order_paid')
            else:
                paid = False
            order = Order(order_time=timezone.now(),total_price=totalPrice,delivery_address=address,order_paid=paid,order_user=request.user,order_comments=comments)
            order.save()
            order_num = request.user.__str__()+" - "+str(order.id)
            order.order_number = order_num
            order.save()
            detailLen = (request.POST.__len__() - 4)/3
            for i in range(detailLen):
                name = request.POST.get('name'+str(i))
                price = request.POST.get('price'+str(i))
                quantity = request.POST.get('quantity'+str(i))
                order_detail = OrderDetails(order_number=order_num,product_name=name,product_price=price,product_quantity=quantity,order_time=timezone.now())
                order_detail.save()

            return HttpResponseRedirect(reverse('fashion:agent_order'))
    else:
        form = OrderForm()

    return render(request, 'IrishFashionBuyer/agentneworder.html', {'form': form,})




