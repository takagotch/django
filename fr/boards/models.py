import math
from django.db import modesl

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='topics')
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
      return self.subject

    def get_page_count(self):
      count = self.posts.count()
      pages = count / 20
      return math.ceil(pages)

    def has_many_pages(self, count=None):
      if count is None:
        count = self.get_page_count()
      return count > 6

    def get_page_range(self):
      count = self.get_page_count()
      if self.has_many_pages(count):
        return range(1, 5)
      return range(1, count + 1)

    def get_last_ten_posts(self):
      return self.posts.order_by('-created_at')[:10]




