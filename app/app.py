from fastapi import FastAPI, HTTPException
from schemas import PostCreate

app = FastAPI()

text_posts = {
    1: {"title": "Test Post", "content": "Cool_posts 101"},
    2: {"title": "Post 2", "content": "post22"},
    3: {"title": "Learning FastAPI", "content": "FastAPI is extremely fast and features automatic documentation."},
    4: {"title": "Python Tips", "content": "Always use type hints for better code clarity and validation."},
    5: {"title": "UV Package Manager", "content": "uv is an extremely fast Python package installer and resolver written in Rust."},
    6: {"title": "Async in Python", "content": "Asynchronous programming helps handle concurrent I/O operations efficiently."},
    7: {"title": "Database ORMs", "content": "Using tools like SQLAlchemy or Drizzle makes database management cleaner."},
    8: {"title": "REST APIs", "content": "RESTful services use standard HTTP methods like GET, POST, PUT, and DELETE."},
    9: {"title": "Environment Variables", "content": "Keep your configuration and API keys safe by using a .env file."},
    10: {"title": "Debugging 101", "content": "Always read error traces carefully from bottom to top to find the root cause."}
}
@app.get("/posts")
def get_all_posts(limit: int=None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="post not found")
    
    return text_posts.get(id)

@app.post("/post")
def create_post(post: PostCreate):
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) +1] = {"title": post.title, "content": post.content}
    return new_post