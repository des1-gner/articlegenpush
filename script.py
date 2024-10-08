import requests
import json
from collections import Counter
from datetime import datetime, timedelta

def fetch_bushfire_news(api_key, days_back=31):
    # API endpoint
    url = "https://newsapi.ai/api/v1/article/getArticles"
    
    # Calculate the date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days_back)
    
    # Construct the query payload
    payload = {
        "query": {
            "$query": {
                "keyword": '(bushfire or bushfires) and ("arson" or "arsonists" or "greens" or "greenies" or "cobargo")',
                "keywordSearchMode": "exact"
            },
            "$filter": {
                "forceMaxDataTimeWindow": str(days_back)
            }
        },
        "resultType": "articles",
        "articlesSortBy": "date",
        "apiKey": api_key
    }
    
    all_articles_info = []
    source_summary = Counter()
    
    try:
        # Make the POST request
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the response
        data = response.json()
        
        if 'articles' in data:
            articles = data['articles'].get('results', [])
            
            for art in articles:
                if isinstance(art, dict):
                    source_name = art.get('source', {}).get('title')
                    if source_name:
                        source_summary[source_name] += 1
                    
                    # Extract and format the publication datetime
                    publication_datetime = art.get('dateTime')
                    if publication_datetime:
                        try:
                            dt = datetime.fromisoformat(publication_datetime.replace('Z', '+00:00'))
                            publication_date = dt.date().isoformat()
                            publication_time = dt.time().isoformat()
                        except ValueError:
                            publication_date = None
                            publication_time = None
                    else:
                        publication_date = None
                        publication_time = None
                    
                    article_info = {
                        'headline': art.get('title'),
                        'published_date': publication_date,
                        'published_time': publication_time,
                        'author': art.get('author'),
                        'source_name': source_name,
                        'content': art.get('body'),
                        'url': art.get('url'),
                        'sentiment': art.get('sentiment')  # NewsAPI.ai provides sentiment analysis
                    }
                    all_articles_info.append(article_info)
                else:
                    print(f"Unexpected article format: {art}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        if hasattr(e.response, 'text'):
            print(f"Response text: {e.response.text}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    return all_articles_info, source_summary

def main():
    # Your API key
    api_key = "5aa21f23-0dd2-4f69-8cdd-8be01239c769"
    
    # Fetch articles
    print("Fetching articles...")
    all_articles_info, source_summary = fetch_bushfire_news(api_key)
    
    # Save the articles
    filename = "BushfireRelatedArticles.json"
    try:
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(all_articles_info, json_file, indent=4, ensure_ascii=False)
        print(f"All articles saved to '{filename}'")
    except Exception as e:
        print(f"Error saving articles to JSON file: {e}")
    
    # Print summary
    print("\nSource summary:")
    for source, count in source_summary.items():
        print(f"{source}: {count} articles")
    
    print(f"\nTotal articles collected: {len(all_articles_info)}")

if __name__ == "__main__":
    main()