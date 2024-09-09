from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator


#post_list renderizado


def post_list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)  # Muestra 5 posts por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

#aquí creas un post y te permite guardarlo



def post_new(request, pk=None):
    if pk:  # Si hay un pk, estamos editando un post existente
        post = get_object_or_404(Post, pk=pk)
    else:
        post = None

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if not post.published_date:
                post.published_date = timezone.now()  # Solo establece la fecha si no está ya establecida
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)  # Si estamos editando, pasa el post existente a la forma

    return render(request, 'blog/post_edit.html', {'form': form})


#aquí te permite editar los post

def post_edit(request, pk=None):
    if pk:
        post = get_object_or_404(Post, pk=pk)
    else:
        post = None

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)  # Añade request.FILES para manejar imágenes
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if not post.published_date:
                post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form})

#Vista de búsqueda

def search(request):
    query = request.GET.get('q', '')  # Obtiene el parámetro de búsqueda
    if query:
        # Busca en los campos 'title' y 'text'
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(text__icontains=query)
        )
    else:
        posts = Post.objects.none()  # Si no hay consulta, no muestra resultados

    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})

#te deja eliminar un post
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Post eliminado con éxito.")
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})


