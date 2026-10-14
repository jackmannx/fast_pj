from fastapi import FastAPI, HTTPException

app = FastAPI()

text_posts = {
    1:{"title": "Test Post", "Content":"Cool_posts 101"},
    2:{"title": "post2", "content": "post22"}
    }

@app.get("/posts")
def get_all_posts():
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="post not found")
    
    return text_posts.get(id)