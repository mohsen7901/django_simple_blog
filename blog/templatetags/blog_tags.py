from django import template
from blog.models import Post, Category, Tag, Comment

register = template.Library()

@register.inclusion_tag('blog/blog-recent-posts.html')
def recent_posts(number=5):
    posts = Post.objects.filter(post_status=True).order_by('-published_date')[:number]
    return {'posts' : posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def post_categories():
    posts = Post.objects.filter(post_status=True)
    categories = Category.objects.all()
    cat_dict = {}
    for c in categories:
        cat_dict[c.name]=posts.filter(categories__name=c.name).count()
    return {'categories':cat_dict}

@register.inclusion_tag('blog/blog-post-tags.html')
def post_tags():
    tags = Tag.objects.all()
    return {'tags':tags}

@register.simple_tag()
def comments_count(pid):
    return Comment.objects.filter(post = pid, is_approved = True).count()