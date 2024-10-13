import random
import feedparser
import textwrap
import ssl


RSS_FEED_URL = "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"


def get_two_news():
    ssl._create_default_https_context = ssl._create_unverified_context
    entries = feedparser.parse(RSS_FEED_URL).entries
    i, j = random.sample(range(len(entries)), 2)
    return entries[i], entries[j]


def brief(rss_entry):
    return {"title": rss_entry.title, "summary": rss_entry.summary}


def get_news(rss_url, num_articles=5):
    # Fix the SSL certificate issue
    ssl._create_default_https_context = ssl._create_unverified_context

    feed = feedparser.parse(rss_url)

    title = "title" in feed.feed and feed.feed.title or "Untitled"
    print(f"Latest news from {title}:\n")

    for entry in feed.entries[:num_articles]:
        print(f"Title: {entry.title}")
        published = ("published" in entry) and entry.published or "[unpublished]"
        print(f"Published: {published}")

        if "summary" in entry:
            summary = textwrap.fill(entry.summary, width=80)
            print(f"Summary: {summary}")

        print(f"Link: {entry.link}\n")
