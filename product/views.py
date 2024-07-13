from typing import Any
from django.shortcuts import render
from django.views import generic
from .models import *
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator, InvalidPage
from django.db.models import Q
from cart.carts import Cart

# Create your views here.

class Home(generic.TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                
                'featured_categories': Category.objects.filter(featured=True),
                'featured_products': Product.objects.filter(featured=True),
                'sliders': Slider.objects.filter(show=True),
                'offers': ShowOffer.objects.filter(show=True),
                'brand': BrandLogo.objects.filter(show=True),
                'featured': Featured.objects.filter(show=True),
            }
        )
        context['current_path'] = self.request.path
        return context
    
    
    
class Product_details(generic.DetailView):
    model = Product
    template_name = 'product_details.html'
    slug_url_kwarg = 'slug'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = self.get_object().related
        
        return context
    
    

    
class Category_details(generic.DetailView):
    model = Category
    template_name = 'category_details.html'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_products'] = self.get_object().products.all()
        return context



class Custom_Paginator:
    def __init__(self, request, queryset, paginated_by):
        self.paginator = Paginator(queryset, paginated_by)
        self.paginated_by = paginated_by
        self.queryset = queryset
        self.page = request.GET.get('page', 1)
        
    def get_queryset(self):
        try:
            queryset = self.paginator.page(self.page)
        except PageNotAnInteger:
            queryset = self.paginator.page(1)
        except EmptyPage:
            queryset = self.paginator.page(1)
        except InvalidPage:
            queryset = self.paginator.page(1)
        
        return queryset
                


class Product_Lists(generic.ListView):
    model = Product
    template_name = 'product_lists.html'
    context_object_name = 'product_lists'
    paginate_by = 1
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_obj = Custom_Paginator(self.request, self.get_queryset(), self.paginate_by)
        queryset = page_obj.get_queryset()
        paginator = page_obj.paginator
        context['product_list'] = queryset
        context['paginator'] = paginator
        context['current_path'] = self.request.path
        
        return context



class Search_Products(generic.View):
    def get(self, *args, **kwargs):
        key = self.request.GET.get('key', '')
        products = Product.objects.filter(
            Q(title__icontains=key) |
            Q(category__title__icontains=key)
        )
        context = {
            'category_products': products,
            'key': key
        }
        
        return render(self.request, 'search_products.html', context)


            
