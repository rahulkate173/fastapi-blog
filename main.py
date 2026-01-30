from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi import templating
from fastapi.staticfiles import StaticFiles
app = FastAPI()
## to serve that statis directory
app.mount("/static",StaticFiles(directory="static"),name="static")
templates = templating.Jinja2Templates("templates")
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
@app.get("/",include_in_schema=False,name="home")
@app.get("/posts",name="posts")
def home(request:Request):
    return templates.TemplateResponse(request,"home.html",{"posts":posts})

@app.get("/api/user")
def api_user():
    return posts

