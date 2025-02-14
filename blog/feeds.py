from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post

class LatestEntriesFeed(Feed):
    title = "latest posts"
    link = "/rss/feed/"
    description = "Latest posts from our blog."

    def items(self):
        return Post.objects.filter(post_status=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:255]
