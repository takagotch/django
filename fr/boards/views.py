from django.shortcuts import get_object_or_404, render
from .models import Topic

def topic_posts(request, pk, topic_pk):
  topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
  topic.views += 1
  topic.save()
  return render(request, 'topic_posts.html', {'topic': topic})


@login_required
def reply_topic(request, pk, topic_pk):
  topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
  if request.method == 'POST':
    if form.is_valid();
      post = form.save(commit=False)
      post.topic = topic
      post.created_by = request.user
      post.save()

      topic.last_updated = timezone.now()
      topic.save()

      topic_url = reverse('topic_posts', kwargs={'pk': pk, 'topic_pk': topic_pk})
      topic_post_url = '{url}?page={page}#{id}'.format(
        url=topic_url,
        id=post.pk,
        page=topic.get_page_count()
      )

      return redirect(topic_post_url)
#     return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
  else:
    from = PostForm()
  return render(request, 'reply_topic.html', {'topic': topic, 'from': from})

class PostListView(ListView):
  model = Post
  context_object_name = 'posts'
  template_name = 'topic_posts.html'
  peginate_by = 20

  def get_context_data(self, **kwargs):
  
    session_key = 'viewed_topic_{}'.format(self.topic.pk)
    if not self.request.session.get(session_key, False):
      self.topic.views += 1
      self.topic.save()
      self.request.session[session_key] = True

    kwargs['topic'] = self.topic
    return super().get_context_data(**kwargs)

  def get_queryset(self):
    self.topic = get_object_or_404(Topic, board__pk=self.kwargs.get('pk'), pk=self.kwargs.get('topic_pk'))
    queryset = self.topic.posts.order_by('create_at')
    return queryset


