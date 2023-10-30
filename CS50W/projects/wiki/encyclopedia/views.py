from django.shortcuts import render
from django.http import HttpResponseRedirect
import markdown2
import random

from . import util

entries = util.list_entries()
data = {
    entry: markdown2.markdown(util.get_entry(entry))
    for entry in entries
}

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": sorted(list(set(entries)))
    })

def getContent(request, name):
    # print(request)
    if name in data:
        html = data[name]
        html += f'<br><a href="../edit/{name}">Edit content</a>'
        return render(request, "encyclopedia/encyclopedia.html", {
            "name": name,
            "html": html
        })
    else:
        html = f'<h1>{name}</h1><p>Sorry, {name} does not exist in wiki!</p>'
        return render(request, "encyclopedia/encyclopedia.html", {
            "name": 'error',
            "html": html
        })
    
def search(request):
    # print(request)
    query = request.GET.get('q')
    header = 'search'
    html = ''

    for entry in entries:
        if entry == query:
            return getContent(request, entry)

    # print(query)
    similar = [entry if query in entry else None for entry in entries]

    for value in similar:
        if value in data:
            html = html + f'<a href="wiki/{value}"><h1>{value}</h1></a>'

    if html == '':
        html = f"Sorry, \"{query}\" does not appear in any documents"
        header = 'error'

    return render(request, "encyclopedia/encyclopedia.html", {
        "name": header,
        "html": html
    })
    
def create(request):
    return render(request, "encyclopedia/create.html", {
        "form_head": '<form method="post" action="/save">',
        "html": '<input placeholder="title" name="title"><br><textarea name="input_text"></textarea><button type="submit">Save</button>',
        "form_tail": '</form>'
    })

def save(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        input_text = request.POST.get('input_text')

        if title not in data and title:
            util.save_entry(title, input_text)
            entries.append(title)
            data[title] = markdown2.markdown(input_text)

            return HttpResponseRedirect(f'/wiki/{title}')
        
        elif not title:
            return render(request, "encyclopedia/encyclopedia.html", {
                "name": "Error",
                "html": f"Error! Please type a meaningful title, ' ' cant be a title"
            })
        
        else:
            return render(request, "encyclopedia/encyclopedia.html", {
                "name": "Error",
                "html": f"Error! {title} is already in use"
            })
        
def editContent(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        input_text = request.POST.get('input_text')
        util.save_entry(title, input_text)
        entries.append(title)
        data[title] = markdown2.markdown(input_text)

        return HttpResponseRedirect(f'/wiki/{title}')
        
        
        
def edit(request, name):
    textMD = util.get_entry(name)
    return render(request, "encyclopedia/edit.html", {
        "form_head": '<form method="post" action="/editContent">',
        "html": f'<input value="{name}" name="title" hidden><textarea name="input_text">{textMD}</textarea><button type="submit">Save</button>',
        "form_tail": '</form>'
    })

def randomPage(request):
    id = random.randint(0, len(entries) - 1)
    name = entries[id]
    # print(name)
    return HttpResponseRedirect(f'/wiki/{name}')