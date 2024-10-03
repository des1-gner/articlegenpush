import json
import random
from datetime import datetime, timedelta

# List of news sources
sources = [
    "Theaustralian.com.au", "Theguardian.com", "Abc.net.au", "News.com.au",
    "Heraldsun.com.au", "Skynews.com.au", "Afr.com", "Smh.com.au",
    "Dailytelegraph.com.au", "Foxnews.com", "Nytimes.com", "Dailywire.com",
    "Couriermail.com.au", "Thewest.com.au", "7news.com.au", "9news.com.au",
    "Theconversation.com", "Nypost.com", "Wsj.com", "Wattsupwiththat.com",
    "Breitbart.com", "Newsmax.com", "Naturalnews.com", "Washingtontimes.com"
]

# Function to generate a random sentence
def random_sentence():
    subjects = ["New study", "Recent report", "Climate scientist", "Environmental group", "Think tank"]
    verbs = ["suggests", "claims", "argues", "reveals", "questions"]
    objects = [
        "global warming trends are exaggerated",
        "climate change impacts are less severe than predicted",
        "natural factors play a larger role in climate change",
        "proposed climate solutions may be ineffective",
        "climate models have significant uncertainties"
    ]
    return f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}."

# Function to generate a random date in the specified format
def random_date():
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    random_date = start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds()))
    )
    return random_date.strftime("%Y-%m-%dT%H:%M:%SZ")

# Define claims and their associated subclaims
claims = {
    "gw_not_happening": {
        "sentence_key": "bc_gw_not_happening_sentence",
        "subclaims": ["sc_cold_event_denial", "sc_deny_extreme_weather"]
    },
    "not_caused_by_human": {
        "sentence_key": "bc_not_caused_by_human_sentence",
        "subclaims": ["sc_natural_variations", "sc_past_climate_reference"]
    },
    "impacts_not_bad": {
        "sentence_key": "bc_impacts_not_bad_sentence",
        "subclaims": ["sc_species_adapt", "sc_downplay_warming"]
    },
    "solutions_wont_work": {
        "sentence_key": "bc_solutions_wont_work_sentence",
        "subclaims": ["sc_policies_negative", "sc_policies_ineffective", "sc_policies_difficult", "sc_low_support_policies", "sc_clean_energy_unreliable"]
    },
    "science_movement_unrel": {
        "sentence_key": "bc_science_movement_unrel_sentence",
        "subclaims": ["sc_climate_science_unrel", "sc_no_consensus", "sc_movement_unreliable", "sc_hoax_conspiracy"]
    },
    "individual_action": {
        "sentence_key": "bc_individual_action_sentence",
        "subclaims": []
    }
}

# Function to generate a random news article
def generate_article():
    source = random.choice(sources)
    content = random_sentence()
    article = {
        "title": {"S": f"Climate Change: {random_sentence()}"},
        "publishedAt": {"S": random_date()},
        "author": {"S": f"{random.choice(['John', 'Jane', 'Alex', 'Sam'])} {random.choice(['Smith', 'Doe', 'Johnson', 'Brown'])}"},
        "urlToImage": {"S": f"https://{source}/images/climate-{random.randint(1000, 9999)}.jpg"},
        "content": {"S": content},
        "description": {"S": f"Brief summary: {content}"}, 
        "sourceName": {"S": source},
        "sourceDescription": {"S": f"A {'leading' if random.random() > 0.5 else 'popular'} news source for {'international' if random.random() > 0.5 else 'national'} news and analysis."},
        "url": {"S": f"https://{source}/article-{random.randint(10000, 99999)}"}
    }

    # Select 1 to 3 random claims
    selected_claims = random.sample(list(claims.keys()), random.randint(1, 3))

    for claim in selected_claims:
        article[claims[claim]["sentence_key"]] = {"S": random_sentence()}
        
        # Select 1 to 3 random subclaims for each claim (if available)
        if claims[claim]["subclaims"]:
            num_subclaims = min(len(claims[claim]["subclaims"]), random.randint(1, 3))
            selected_subclaims = random.sample(claims[claim]["subclaims"], num_subclaims)
            
            for subclaim in selected_subclaims:
                article[f"{subclaim}_sentence"] = {"S": random_sentence()}

    # Add think tank reference with 30% probability
    if random.random() < 0.3:
        article["think_tank_ref_sentence"] = {"S": random_sentence()}

    return article

# Generate 200 articles
articles = [generate_article() for _ in range(200)]

# Save to JSON file
with open('climate_news_data.json', 'w') as f:
    json.dump(articles, f, indent=2)

print("Generated 200 articles and saved to climate_news_data.json")
