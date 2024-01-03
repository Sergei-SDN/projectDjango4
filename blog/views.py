from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify
from django.core.mail import send_mail
from blog.forms import BlogForm
from blog.models import Blog


# Create your views here.


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_nat = form.save()
            new_nat.slug = slugify(new_nat.title)
            new_nat.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    form_class = BlogForm

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.views == 99:
            send_mail(
                'Поздравляем! Ваша статья достигла 100 просмотров!',
                'Поздравляем! Ваша статья достигла 100 просмотров!',
                'your_email@example.com',
                ['recipient@example.com'],
                fail_silently=False,
            )
        self.object.views += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm

    # success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_nat = form.save()
            new_nat.slug = slugify(new_nat.title)
            new_nat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
