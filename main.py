from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from random import randrange
from model import Post

app = FastAPI()

# Array to store data in memory
my_posts = [
    {
        "title": "Black Panther",
        "content": "Marvel african superhero story",
        "rating": 6.4,
        "id": 1,
    },
    {
        "title": "Top Gun : Maverick",
        "content": "Senior Navy Pilot trains promising young aviators",
        "rating": 9.0,
        "id": 2,
    },
]
def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

# routes or path operations
@app.get("/")
async def root():
    return {"message": "Hello and welcome to my page"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

# Single user
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} was not found"
            )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message': f'Post with id {id} was not found'}
    return {"post_data": f"{post}"}




@app.post("/posts")
def create_posts(new_post: Post):
    post_dict = new_post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}
