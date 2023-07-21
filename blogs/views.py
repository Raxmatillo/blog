from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from colorthief import ColorThief

from .models import Category, Blog


from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin



def home(request):
	q = request.GET.get('q') if request.GET.get('q') != None else ''
	print(q)
	blogs = Blog.objects.filter(
		Q(title__icontains=q) |
		Q(blog_subcategory__icontains=q) |
		Q(summary__icontains=q)
	)

	categories = Category.objects.all()
	
	paginator = Paginator(blogs, 8)
	page_number = request.GET.get('page')
	blogs = paginator.get_page(page_number)


	blogs_views = Blog.objects.all()


	if len(blogs_views) == 1:
		main_blog = Blog.objects.all().last()
	if len(blogs_views)>1:
		main_blog = Blog.objects.filter(base_blog=True)[0]
	if len(blogs_views)<1:
		return render(request, 'default.html')

	

	color_thief = ColorThief("."+main_blog.photo.url)
	dominant_color = color_thief.get_color()



	
	context = {
		'categories': categories,
		'blogs': blogs,
		'blogs_views': blogs_views,
		'main_blog': main_blog,
		'dominant_color': dominant_color,
		'r': dominant_color[0],
		'g': dominant_color[1],
		'b': dominant_color[2],
	}
	

	return render(request, 'home.html', context)


def detail(request, slug=None):
	q = request.GET.get('q') if request.GET.get('q') != None else ''

	blogs = Blog.objects.filter(
		Q(title__icontains=q) |
		Q(blog_subcategory__icontains=q) |
		Q(summary__icontains=q)
	)

	
	paginator = Paginator(blogs, 2)
	page_number = request.GET.get('page')
	blogs = paginator.get_page(page_number)

	blog = Blog.objects.get(slug=slug)

	# hitcount
	hit_count = get_hitcount_model().objects.get_for_object(blog)
	hits = hit_count.hits
	hit_count_response = HitCountMixin.hit_count(request, hit_count)
	if hit_count_response.hit_counted:
		hits +=1

	blogs_views = Blog.objects.all()

	if len(blogs_views) == 1:
		main_blog = Blog.objects.all().last()
	else:
		main_blog = Blog.objects.filter(base_blog=True)[0]
	if len(blogs_views)<1:
		return render(request, 'default.html')
	
	
	categories = Category.objects.all()

	color_thief = ColorThief("."+main_blog.photo.url)
	dominant_color = color_thief.get_color()

	context = {
		'categories': categories,
		'blogs': blogs,
		'blogs_views': blogs_views,
		'main_blog': main_blog,
		'blog':blog,
		'hits':hits,
		'dominant_color': dominant_color,
		'r': dominant_color[0],
		'g': dominant_color[1],
		'b': dominant_color[2],
	}
	return render(request, 'detail.html', context)




def custom_404_view(request):
    return render(request, '404.html')