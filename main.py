# frontend with jinja templates

from fastapi import FastAPI, Request #request  is required by jinja
#we dont need HTMLResponse now that we have jinja2templates
from fastapi.templating import Jinja2Templates #jinja2templates for templating

posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]

app = FastAPI() #this app object will be use to define the whole route
templates = Jinja2Templates(directory="templates") #here we defined where to find the templates for templating you know what i mean
@app.get("/",include_in_schema=False) #here it will gonna trigger the home route
@app.get("/posts",include_in_schema=False) #here we stacked the decorator for us to access same data from diff route 
def home(request: Request): #jinja need request param for doing stuff
    return templates.TemplateResponse(
        request, 
        "home.html", 
        {"posts": posts, "title": "Home"}) #requesting our template to run
#with template  can display the post and title

@app.get("/api/posts")
def get_post():
    return posts


