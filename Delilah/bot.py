#!/usr/bin/python
import os

import praw
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("client_id")
CLIENT_SECRET = os.getenv("client_secret")
PASSWORD = os.getenv("PASSWORD")
USERNAME = os.getenv("username")

# reddit = praw.Reddit('delilah')
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    password=PASSWORD,
    user_agent="Comment Extraction (by u/USERNAME)",
    username=USERNAME,
)

subreddit = reddit.subreddit("learnpython")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")
