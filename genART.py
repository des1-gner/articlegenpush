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

#import json
import random
import string
from datetime import datetime, timedelta

# (Previous code for sources, subjects, verbs, topics, descriptors, consequences remains unchanged)

# Updated claims structure
broadClaims = {
    "gw_not_happening": "Global warming is not happening",
    "not_caused_by_human": "Climate change is not caused by human activities",
    "impacts_not_bad": "Climate change impacts are not that bad",
    "solutions_wont_work": "Climate solutions won't work",
    "science_movement_unrel": "Climate science or movement is unreliable",
    "individual_action": "Individual action is pointless"
}

subClaims = {
    "sc_cold_event_denial": "Cold weather event disproves global warming",
    "sc_deny_extreme_weather": "Extreme weather events are not increasing",
    "sc_natural_variations": "Climate change is due to natural variations",
    "sc_past_climate_reference": "Past climate changes prove current changes are natural",
    "sc_species_adapt": "Species can adapt to climate change",
    "sc_downplay_warming": "Warming is not as bad as predicted",
    "sc_policies_negative": "Climate policies have negative consequences",
    "sc_policies_ineffective": "Climate policies are ineffective",
    "sc_policies_difficult": "Climate policies are too difficult to implement",
    "sc_low_support_policies": "There is low public support for climate policies",
    "sc_clean_energy_unreliable": "Clean energy sources are unreliable",
    "sc_climate_science_unrel": "Climate science is unreliable",
    "sc_no_consensus": "There is no scientific consensus on climate change",
    "sc_movement_unreliable": "The climate movement is unreliable",
    "sc_hoax_conspiracy": "Climate change is a hoax or conspiracy"
}

# Mapping between broad claims and subclaims
claim_mapping = {
    "gw_not_happening": ["sc_cold_event_denial", "sc_deny_extreme_weather"],
    "not_caused_by_human": ["sc_natural_variations", "sc_past_climate_reference"],
    "impacts_not_bad": ["sc_species_adapt", "sc_downplay_warming"],
    "solutions_wont_work": ["sc_policies_negative", "sc_policies_ineffective", "sc_policies_difficult", "sc_low_support_policies", "sc_clean_energy_unreliable"],
    "science_movement_unrel": ["sc_climate_science_unrel", "sc_no_consensus", "sc_movement_unreliable", "sc_hoax_conspiracy"],
    "individual_action": []
}

# Updated function to generate a random news article
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
        "uri": {"S": generate_uri()},
        "isDuplicate": {"BOOL": random.random() < 0.05},  # 5% chance of being a duplicate
        "broadClaims": {"M": {}},
        "subClaims": {"M": {}}
    }

    # Select 1 to 3 random broad claims
    num_broad_claims = random.randint(1, 3)
    selected_broad_claims = random.sample(list(broadClaims.keys()), num_broad_claims)

    for bc in selected_broad_claims:
        article["broadClaims"]["M"][bc] = {"S": random_sentence()}
        
        # Select 0 to 3 subclaims for each broad claim
        available_subclaims = claim_mapping[bc]
        if available_subclaims:
            num_subclaims = random.randint(0, min(3, len(available_subclaims)))
            selected_subclaims = random.sample(available_subclaims, num_subclaims)
            
            for sc in selected_subclaims:
                article["subClaims"]["M"][sc] = {"S": random_sentence()}

    # Remove empty maps to comply with DynamoDB requirements
    if not article["broadClaims"]["M"]:
        del article["broadClaims"]
    if not article["subClaims"]["M"]:
        del article["subClaims"]

    # Add think tank reference with 30% probability
    if random.random() < 0.3:
        article["think_tank_ref"] = {"S": random_sentence()}

    return article

# Generate 500 articles
articles = [generate_article(i) for i in range(500)]

# Save to JSON file
with open('climate_news_data.json', 'w') as f:
    json.dump(articles, f, indent=2)

print("Generated 500 articles and saved to climate_news_data.json")

# Print a sample article to verify the structure
print("\nSample article structure:")
print(json.dumps(articles[0], indent=2))