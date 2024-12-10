from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse


# posts is a list with elements as dictionary
posts=[
    {
        "id": 1,
        "title": "Python",
        "content": "A versatile high-level programming language used for web development, data analysis, AI, and more."
    },
    {
        "id": 2,
        "title": "JavaScript",
        "content": "A popular language for web development, used to create interactive and dynamic web applications."
    },
    {
        "id": 3,
        "title": "Java",
        "content": "A robust object-oriented programming language commonly used in enterprise-level applications and Android development."
    }
]

# Create your views here.
def home(request):     #first view we created
    # print(reverse('home',args=['ravi']))

    # html=""
    # for post in posts:
    #     html+=f'''
    #     <div>
    #     <a href="posts/{post['id']}/">
    #         <h1>{post['id']}-{post['title']}</h1></a>
    #         <p>{post['content']}</p>
    #     </div>'''
        

# Key Difference
# Relative Path (posts/{post['id']}/): May vary depending on the current page's URL, which could lead to broken links in nested routes.
# Absolute Path (/posts/{post['id']}/): Always works as expected because it starts from the domain root.
# Best Practice
# Use the absolute path (/posts/{post['id']}/) for consistency and to avoid issues when linking from different parts of your website.

    html2=''
    for post in posts:
        # the anchor tag below is an absolute path
        html2+=f'''
        <div> 
            <a href="/posts/{post['id']}/">   
           
            {post['id']}-{post['title']}</a>
            <p>{post['title']}-{post['content']}</div>'''
        
    name="Ranjith"

    # return render(request,"posts/home.html",{"rag":html})
    return HttpResponse(html2)
    # return render(request,"posts/home.html",{"posts":posts,"name":name})
    # return render(request,"posts/home.html")



def post(request,id):                 # view about dynamic url
    # print(type(id))
    valid_id=False
    for post in posts:
        if post['id']==id:
           post_dict=post
           valid_id=True
           break
    if valid_id==True:
        html=f'''
                <h1>{post_dict['title']}</h1>
                <p>{post_dict['content']}</p>
                '''
  
        return HttpResponse(html)
    else:
        return HttpResponseNotFound("Post not Available")
    

def google(request,id):
    url=reverse("post",args=[id])
    print(url)
    return HttpResponseRedirect(url)


def viva(request):
    return render(request,"posts/viva.html")


