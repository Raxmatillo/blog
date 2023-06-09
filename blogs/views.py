from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render



from .models import Category, Blog




def home(request):
	q = request.GET.get('q') if request.GET.get('q') != None else ''

	blogs = Blog.objects.filter(
		Q(title__icontains=q) |
		Q(blog_subcategory__icontains=q) |
		Q(summary__icontains=q)
	)

	paginator = Paginator(blogs, 2)
	page_number = request.GET.get('page')
	blogs = paginator.get_page(page_number)


	blogs_views = Blog.objects.all().order_by("-views")[:5]
	main_blog = Blog.objects.filter(base_blog=True)[0]
	categories = Category.objects.all()
	print(main_blog)
	context = {
		'categories': categories,
		'blogs': blogs,
		'blogs_views': blogs_views,
		'main_blog': main_blog
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
	blogs_views = Blog.objects.all().order_by("-views")[:5]
	main_blog = Blog.objects.filter(base_blog=True)[0]
	categories = Category.objects.all()
	context = {
		'categories': categories,
		'blogs': blogs,
		'blogs_views': blogs_views,
		'main_blog': main_blog,
		'blog':blog
	}
	return render(request, 'detail.html', context)