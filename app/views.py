from django.shortcuts import *
from django.http import *
from .models import Crypto, Comment
from .forms import *
from django.template.loader import *
from django.views.decorators.http import require_http_methods

def get_by_slug(request, slug):
    crypto = Crypto.objects.get(slug=slug)
    return HttpResponse(render(request, 'crypto1.html', {'crypto':crypto}))

def get_comments(request):
    return HttpResponse(render(request, 'comments.html', {'comments': Comment.objects.all}))

def get_comment(request, comment_id):
    comment_id = Comment.objects.get(id=comment_id)
    return HttpResponse(render(request, 'comment.html', {'comment':comment_id}))

def delete_comment(request, comment_id):
    comment_id = Comment.objects.get(id=comment_id)
    comment_id.delete()
    return HttpResponse(render(request, 'comment_deleted.html'))

def create_comment(request):
    if request.method == 'POST':
        content = request.POST['content']
        author = request.POST['author']
        Comment.objects.create(content=content, author=author)
        return redirect('/comments/create')
    else:
        return HttpResponse(render(request, 'comment_create.html'))

def add(request):
    cf = CommentForm
    context = {'form': cf}
    return render(request, 'comment_create.html', context)

def add_save(request):
    cf = CommentForm(request.POST)
    if cf.is_valid():
        cf.save()
        return HttpResponseRedirect(reverse('get_comments'))
    else:
        context = {'form': cf}
        return render(request, 'comment_create.html', context)

def add_and_save(request):
    if request.method == 'POST':
        cf = CommentForm(request.POST)
        if cf.is_valid():
            cf.save()
            return HttpResponseRedirect(reverse('get_comments'))
        else:
            context = {'form': cf}
            return render(request, 'comment_create.html', context)
    else:
        cf = CommentForm
        context = {'form': cf}
        return render(request, 'comment_create.html', context)

def index_view(request):
    res = HttpResponse("Here will be", content_type='text/plain; scharset=utf-8')
    res.write('main')
    res.writelines(('web', 'site'))
    res['keywords'] = 'Python Django'
    return res

def index_view2(request):
    cr = Crypto.objects.all()
    context = {'cr': cr}
    template = get_template('index_view.html')
    return HttpResponse(template.render(context=context, request=request))

def index_view3(request):
    cr = Crypto.objects.all()
    context = {'cr': cr}
    return HttpResponse(render_to_string('index_view.html', context, request))

def detail(request, id):
    try:
        cm = Comment.objects.get(id=id)
    except Comment.DoesNotExist:
        raise Http404("Comment does not exist")
    
    print(request.method)
    print(request.scheme)
    print(request.headers)
    print("          ")
    print(request.get_host())
    print(request.get_port())
    print(request.get_full_path())
    return HttpResponse(cm.content)

def json_response_view(request):
    data = {
        'message': 'This is a JSON response',
        'status': 'success'
    }
    return JsonResponse(data)

def redirect_view(request):
    return redirect('index_view3') 

@require_http_methods(["GET"])
def only_get_view(request):
    return JsonResponse({'message': 'Только GET-запросы разрешены'}, json_dumps_params={'ensure_ascii': False}) 
