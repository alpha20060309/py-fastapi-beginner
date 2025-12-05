from fastapi import FastAPI, HTTPException
from src.schema import PostCreate
from src.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

text_posts = {
    1: {
        "title": "Exploring FastAPI for Building APIs",
        "content": "FastAPI is a modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints."
    },
    2: {
        "title": "Python 3.12 Released!",
        "content": "The Python Software Foundation has released Python 3.12 with new optimizations, syntax features, and improved error messages."
    },
    3: {
        "title": "Tips for Effective Remote Work",
        "content": "Maintain a regular schedule, invest in a comfortable workspace, and communicate proactively with your team."
    },
    4: {
        "title": "How to Cook Perfect Rice",
        "content": "Rinse your rice before cooking, use the right water-to-rice ratio, and let it rest after cooking for fluffy grains."
    },
    5: {
        "title": "Best Hiking Trails in California",
        "content": "Yosemite's Mist Trail, Mount Tamalpais, and the Lost Coast Trail are top picks for breathtaking hikes."
    },
    6: {
        "title": "Understanding Artificial Intelligence",
        "content": "AI is a field of computer science that aims to create systems capable of performing tasks that usually require human intelligence."
    },
    7: {
        "title": "Upcoming Tech Conferences 2024",
        "content": "Attend CES in Las Vegas, PyCon US in Pittsburgh, or Web Summit in Lisbon for networking and learning opportunities."
    },
    8: {
        "title": "Simple Vegan Pancake Recipe",
        "content": "Mix flour, plant milk, baking powder, and a dash of salt. Cook on a skillet until bubbles form, then flip."
    },
    9: {
        "title": "Improving Mental Health",
        "content": "Practice mindfulness, stay connected with friends, and seek professional help if experiencing ongoing stress or sadness."
    },
    10: {
        "title": "Guide to Investing for Beginners",
        "content": "Start with index funds, diversify your portfolio, and invest regularly for long-term growth."
    }
}


@app.get("/posts")
def get__all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts[id]

@app.post("/posts")
def create_post(post: PostCreate) -> PostCreate:
    new_post = {"title": post.title, "content": post.content}
    text_posts[len(text_posts.keys()) + 1] = new_post
    return new_post
