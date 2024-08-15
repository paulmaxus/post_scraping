from facebook_scraper import get_posts
import pandas as pd


with open('pages.txt', 'r') as f:
    pages = f.read().split('\n')

def extract(page):

    post_gen = get_posts(
        page, 
        base_url="https://mbasic.facebook.com", 
        start_url=f"https://mbasic.facebook.com/{page}?v=timeline",
        cookies = 'cookies.json',
        pages = 1,
        options = {
            #"posts_per_page": 1,  # seems to return all posts, no matter what
            #"reactions": True,  # means more requests
            "allow_extra_requests": True
        }
    )

    posts = [] 
    for post in post_gen:
        post_id = str(post.get('post_id'))
        post_time = post.get('time')
        post_text = post.get('full_text')
        if not post_text:
            post_text = post.get('text')
        post_n_comments = post.get('comments')
        post_n_likes = post.get('likes')
        post_reactions = post.get('reactions')
        posts.append({
            'page': page, 
            'id': post_id, 
            'time': post_time, 
            'comments': post_n_comments, 
            'likes': post_n_likes, 
            'reactions': post_reactions, 
            'text': post_text,
        })

    return posts

data = []
for page in pages:
    posts = extract(page)
    data.extend(posts)

pd.DataFrame(data).to_csv('posts.csv', index=False)
	