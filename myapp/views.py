from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from django.core.paginator import Paginator
from django.shortcuts import render,redirect, get_object_or_404
from .forms import *
from cart.forms import CartAddProductForm













def handler404(request, exception):
    return render(request, 'myapp/core/404.html', status=404)

def handler500(request):
    return render(request, 'myapp/core/500.html', status=500)





class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'myapp/register.html'
    success_url = reverse_lazy('register')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'myapp/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('login')


def logout_user(request):
    logout(request)
    return redirect('login')













def show_category(request, cat_id):
    product = Product.objects.filter(cat_id=cat_id).order_by('-id')
    cats = Category.objects.all()
    paginator = Paginator(product, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if len(product) == 0:
        raise Http404()

    context = {'page_obj': page_obj,'product': product, 'cats': cats, 'cat_selected': cat_id}
    return render(request, 'myapp/menu.html', context=context)


class ProductListView(ListView):
    model = Product
    paginate_by = 8
    template_name = 'myapp/menu.html'
    context_object_name = 'products'
    queryset = Product.objects.all()

def index(request):
    product = Product.objects.all().order_by('-id')
    cats = Category.objects.all()
    context = {'product': product, 'cats': cats, 'cat_selected': 0}
    return render(request, 'myapp/index.html', context)

def menu(request):
    product = Product.objects.all().order_by('-id')
    cats = Category.objects.all()
    paginator = Paginator(product, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cart_product_form = CartAddProductForm()
    context = {'page_obj': page_obj, 'product': product, 'cats': cats, 'cat_selected': 0, 'cart_product_form': cart_product_form}
    return render(request, 'myapp/menu.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'myapp/menu.html', {'product': product,
                                                        'cart_product_form': cart_product_form})


def action(request):
    return render(request, 'myapp/action.html')




def test(request):
    product = Product.objects.all().order_by('-id')
    cart_product_form = CartAddProductForm()
    context = {'product': product, 'cart_product_form': cart_product_form}
    return render(request, 'myapp/test.html', context)

def test_modal(request):
    product = Product.objects.all().order_by('-id')
    cart_product_form = CartAddProductForm()
    context = {'product': product, 'cart_product_form': cart_product_form}
    return render(request, 'myapp/test/test-modal.html', context)
