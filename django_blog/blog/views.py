# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Post, Comment
from .forms import PostForm, CommentForm, CustomUserCreationForm

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect("profile")
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})

@login_required
def profile(request):
    if request.method == "POST":
        user = request.user
        user.email = request.POST.get("email")
        user.save()
        return redirect("profile")
    return render(request, "blog/profile.html")

def custom_logout(request):
    logout(request)
    return redirect("login")

# Post CRUD Views
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        context["comments"] = self.object.comments.all()
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Comment CRUD Views
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs["post_id"])
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.kwargs["post_id"]})

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"
    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.object.post.pk})
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"
    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.object.post.pk})
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

class PostByTagListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    def get_queryset(self):
        tag = self.kwargs["tag_slug"]  # Changed from "tag" to "tag_slug"
        return Post.objects.filter(tags__slug=tag)  # Changed from tags__name__in to tags__slug

class SearchView(ListView):
    model = Post
    template_name = "blog/search_results.html"
    context_object_name = "posts"
    def get_queryset(self):
        query = self.request.GET.get("q", "")
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)  
            ).distinct()
        return Post.objects.none()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        return context