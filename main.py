import datetime

def extract_news_data():
    """
    Simulates extracting raw news data from a source.
    In a real-world scenario, this would involve API calls, web scraping, or database queries.
    """
    # Simulate raw news data from a hypothetical news API
    raw_articles = [
        {
            "id": "news-101",
            "source": {"name": "TechCrunch"},
            "author": "John Doe",
            "title": "Python 4.0 Released with Async Improvements",
            "description": "The new version of Python brings significant enhancements to asynchronous programming.",
            "url": "http://example.com/python4",
            "publishedAt": "2023-10-26T10:00:00Z",
            "content": "Python 4.0 is here..."
        },
        {
            "id": "news-102",
            "source": {"name": "BBC News"},
            "author": None,
            "title": "Global Economy Outlook 2024",
            "description": "Experts weigh in on the economic predictions for the coming year.",
            "url": "http://example.com/economy",
            "publishedAt": "2023-10-25T15:30:00Z",
            "content": "Economists predict..."
        },
        {
            "id": "news-103",
            "source": {"name": "The Verge"},
            "author": "Jane Smith",
            "title": None, # Missing title
            "description": "A new smartphone was announced today with groundbreaking camera technology.",
            "url": "http://example.com/smartphone",
            "publishedAt": "2023-10-26T09:15:00Z",
            "content": "The new phone..."
        },
        {
            "id": "news-104",
            "source": {"name": "CNN"},
            "author": "Reporter A",
            "title": "Climate Change Summit Concludes",
            "description": None, # Missing description
            "url": "http://example.com/climate",
            "publishedAt": "2023-10-24T18:00:00Z",
            "content": "Leaders discussed..."
        }
    ]
    print("--- EXTRACTED RAW DATA ---")
    for article in raw_articles:
        print(f"  ID: {article['id']}, Title: {article.get('title')}, Desc: {article.get('description')}")
    print("\n")
    return raw_articles

def transform_news_data(raw_articles):
    """
    Transforms raw news data into a clean, structured format.
    This includes filtering, cleaning, and standardizing data.
    """
    transformed_articles = []
    for article in raw_articles:
        # --- TRANSFORM: Filter out articles with missing essential fields (title or description) ---
        if not article.get("title") or not article.get("description"):
            print(f"  Skipping article {article.get('id')} due to missing title or description.")
            continue

        # --- TRANSFORM: Standardize and clean data fields ---
        processed_article = {
            "article_id": article["id"],
            "source_name": article["source"]["name"],
            "author": article.get("author") if article.get("author") else "Unknown",
            "title": article["title"].strip(),
            "description": article["description"].strip(),
            "url": article["url"],
            # --- TRANSFORM: Convert published date to a consistent ISO 8601 format ---
            "published_at": datetime.datetime.fromisoformat(article["publishedAt"].replace('Z', '+00:00')).isoformat(),
            "processed_at": datetime.datetime.now().isoformat() # --- TRANSFORM: Add a processing timestamp ---
        }
        transformed_articles.append(processed_article)

    print("--- TRANSFORMED DATA ---")
    for article in transformed_articles:
        print(f"  ID: {article['article_id']}, Title: {article['title']}, Processed: {article['processed_at']}")
    print("\n")
    return transformed_articles

def load_news_data(transformed_articles):
    """
    Simulates loading transformed news data into a destination.
    In a real-world scenario, this would involve inserting into a database (like PostgreSQL),
    writing to a file, or sending to a message queue.
    """
    print("--- LOADED DATA (Simulated to Console) ---")
    if not transformed_articles:
        print("  No articles to load.")
        return

    for article in transformed_articles:
        # --- LOAD: Print to console as a simulation of storing in a database ---
        print(f"  Loading Article ID: {article['article_id']}")
        print(f"    Title: {article['title']}")
        print(f"    Source: {article['source_name']}")
        print(f"    Published: {article['published_at']}")
        print(f"    Processed: {article['processed_at']}")
        print("-" * 20)
    print("\n")

if __name__ == "__main__":
    print("Starting ETL pipeline simulation for news data...\n")

    # 1. Extract: Get raw data from a source
    raw_data = extract_news_data()

    # 2. Transform: Clean and structure the raw data
    cleaned_data = transform_news_data(raw_data)

    # 3. Load: Store the transformed data into a destination
    load_news_data(cleaned_data)

    print("ETL pipeline simulation complete.")
