import json
import random
import string
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

# Expanded word lists for more varied content generation
subjects = [
    "New study", "Recent report", "Climate scientist", "Environmental group", "Think tank",
    "Research team", "Government report", "Scientific analysis", "Expert panel", "International study",
    "Leading researcher", "Climate observatory", "Weather station", "Satellite data", "Computer model",
    "Statistical analysis", "Field research", "Laboratory experiment", "Long-term study", "Meta-analysis",
    "Industry report", "Academic paper", "Policy brief", "Working group", "Research consortium"
]

verbs = [
    "suggests", "claims", "argues", "reveals", "questions",
    "indicates", "demonstrates", "shows", "proves", "implies",
    "confirms", "challenges", "contradicts", "validates", "disputes",
    "reinforces", "undermines", "establishes", "refutes", "supports"
]

topics = [
    "global warming trends", "climate change impacts", "temperature records",
    "sea level rise", "extreme weather events", "greenhouse gas emissions",
    "arctic ice melting", "ocean acidification", "renewable energy adoption",
    "carbon dioxide levels", "methane emissions", "climate policy effectiveness",
    "environmental regulations", "fossil fuel industry", "clean energy transition",
    "climate modeling accuracy", "weather pattern changes", "ecosystem impacts",
    "agricultural effects", "economic implications"
]

descriptors = [
    "significant", "minimal", "unprecedented", "gradual", "dramatic",
    "unexpected", "controversial", "established", "theoretical", "practical",
    "concerning", "reassuring", "alarming", "encouraging", "questionable",
    "definitive", "inconclusive", "preliminary", "comprehensive", "limited"
]

consequences = [
    "requiring immediate action", "suggesting policy changes", "demanding further study",
    "challenging previous assumptions", "supporting existing theories",
    "indicating potential risks", "revealing new opportunities", "affecting global markets",
    "impacting future predictions", "altering scientific consensus",
    "prompting renewed debate", "necessitating additional research",
    "raising important questions", "changing public perception",
    "influencing policy decisions"
]

# Function to generate a more complex random sentence
def random_sentence():
    pattern = f"{random.choice(subjects)} {random.choice(verbs)} that {random.choice(topics)} are {random.choice(descriptors)}, {random.choice(consequences)}."
    return pattern

# Function to generate a more complex random sentence for titles
def random_title():
    patterns = [
        f"New {random.choice(topics)}: {random.choice(descriptors)} findings {random.choice(consequences)}",
        f"Study: {random.choice(topics)} show {random.choice(descriptors)} trends",
        f"Report: {random.choice(descriptors)} changes in {random.choice(topics)}",
        f"Analysis reveals {random.choice(descriptors)} {random.choice(topics)}",
        f"Expert: {random.choice(topics)} {random.choice(verbs)} {random.choice(descriptors)} shift"
    ]
    return random.choice(patterns)

# Function to generate a longer, more varied body text
def generate_body():
    paragraphs = []
    num_paragraphs = random.randint(3, 6)
    
    for _ in range(num_paragraphs):
        sentences = []
        num_sentences = random.randint(4, 8)
        
        for _ in range(num_sentences):
            pattern = random.choice([
                f"{random.choice(subjects)} {random.choice(verbs)} that {random.choice(topics)} are {random.choice(descriptors)}, {random.choice(consequences)}.",
                f"According to {random.choice(subjects)}, {random.choice(topics)} have shown {random.choice(descriptors)} changes, {random.choice(consequences)}.",
                f"The {random.choice(descriptors)} nature of {random.choice(topics)} {random.choice(verbs)} {random.choice(consequences)}.",
                f"Researchers studying {random.choice(topics)} have found {random.choice(descriptors)} evidence {random.choice(consequences)}."
            ])
            sentences.append(pattern)
        
        paragraphs.append(" ".join(sentences))
    
    return "\n\n".join(paragraphs)

# Function to generate a random date in the specified range
def random_date():
    start_date = datetime(2019, 9, 1)
    end_date = datetime(2020, 4, 1)
    random_date = start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds()))
    )
    return random_date.strftime("%Y-%m-%dT%H:%M:%SZ")

# Function to generate author (with 25% chance of being empty)
def generate_author():
    if random.random() < 0.25:
        return {"S": ""}
    first_names = ['John', 'Jane', 'Alex', 'Sam', 'Michael', 'Sarah', 'David', 'Emma', 
                  'James', 'Linda', 'Robert', 'Patricia', 'Daniel', 'Elizabeth']
    last_names = ['Smith', 'Doe', 'Johnson', 'Brown', 'Davis', 'Miller', 'Wilson', 
                 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White']
    return {"S": f"{random.choice(first_names)} {random.choice(last_names)}"}

# Function to generate a random URI string
def generate_uri():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"uri-{random_string}"

# Claims dictionary
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
def generate_article(article_id):
    source = random.choice(sources)
    article = {
        "articleId": {"N": str(article_id)},
        "title": {"S": random_title()},
        "dateTime": {"S": random_date()},
        "authors": generate_author(),
        "image": {"S": f"https://{source}/images/climate-{random.randint(1000, 9999)}.jpg"},
        "body": {"S": generate_body()},
        "source": {"S": source},
        "url": {"S": f"https://{source}/article-{random.randint(10000, 99999)}"},
        "uri": {"S": generate_uri()}  # Adding the uri field
    }

    # Select 1 to min(3, number of available claims) random claims
    num_claims = min(3, len(claims))
    num_claims_to_select = random.randint(1, num_claims)
    selected_claims = random.sample(list(claims.keys()), num_claims_to_select)

    for claim in selected_claims:
        article[claims[claim]["sentence_key"]] = {"S": random_sentence()}
        
        # Only attempt to add subclaims if they exist
        if claims[claim]["subclaims"]:
            num_available_subclaims = len(claims[claim]["subclaims"])
            if num_available_subclaims > 0:
                num_subclaims = min(3, num_available_subclaims)
                num_subclaims_to_select = random.randint(1, num_subclaims)
                selected_subclaims = random.sample(claims[claim]["subclaims"], num_subclaims_to_select)
                
                for subclaim in selected_subclaims:
                    article[f"{subclaim}_sentence"] = {"S": random_sentence()}

    # Add think tank reference with 30% probability
    if random.random() < 0.3:
        article["think_tank_ref_sentence"] = {"S": random_sentence()}

    return article

# Generate 500 articles
articles = [generate_article(i) for i in range(500)]

# Save to JSON file
with open('climate_news_data.json', 'w') as f:
    json.dump(articles, f, indent=2)

print("Generated 500 articles and saved to climate_news_data.json")
