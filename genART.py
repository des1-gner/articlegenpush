import json
import random
import string
from datetime import datetime, timedelta

# List of news sources (lowercase)
sources = [
    "theaustralian.com.au", "theguardian.com", "abc.net.au", "news.com.au",
    "heraldsun.com.au", "skynews.com.au", "afr.com", "smh.com.au",
    "dailytelegraph.com.au", "foxnews.com", "nytimes.com", "dailywire.com",
    "couriermail.com.au", "thewest.com.au", "7news.com.au", "9news.com.au",
    "theconversation.com", "nypost.com", "wsj.com", "wattsupwiththat.com",
    "breitbart.com", "newsmax.com", "naturalnews.com", "washingtontimes.com"
]

# Expanded word lists for more varied content generation (lowercase)
subjects = [
    "new study", "recent report", "climate scientist", "environmental group", "think tank",
    "research team", "government report", "scientific analysis", "expert panel", "international study",
    "leading researcher", "climate observatory", "weather station", "satellite data", "computer model",
    "statistical analysis", "field research", "laboratory experiment", "long-term study", "meta-analysis",
    "industry report", "academic paper", "policy brief", "working group", "research consortium"
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
    "agricultural effects", "economic implications",
    "wildfire frequency", "bushfire intensity", "arson allegations",
    "forest management practices", "greenies' influence", "smog levels",
    "bush regeneration", "koala habitat loss", "australian climate patterns",
    "california drought conditions", "geological climate indicators",
    "human-induced climate change", "natural climate variability"
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

# Function to generate a more complex random sentence (lowercase)
def random_sentence():
    pattern = f"{random.choice(subjects)} {random.choice(verbs)} that {random.choice(topics)} are {random.choice(descriptors)}, {random.choice(consequences)}."
    return pattern.lower()

# Function to generate a more complex random sentence for titles (lowercase)
def random_title():
    patterns = [
        f"new {random.choice(topics)}: {random.choice(descriptors)} findings {random.choice(consequences)}",
        f"study: {random.choice(topics)} show {random.choice(descriptors)} trends",
        f"report: {random.choice(descriptors)} changes in {random.choice(topics)}",
        f"analysis reveals {random.choice(descriptors)} {random.choice(topics)}",
        f"expert: {random.choice(topics)} {random.choice(verbs)} {random.choice(descriptors)} shift"
    ]
    return random.choice(patterns).lower()

# Function to generate a longer, more varied body text (lowercase)
def generate_body():
    paragraphs = []
    num_paragraphs = random.randint(3, 6)
    
    for _ in range(num_paragraphs):
        sentences = []
        num_sentences = random.randint(4, 8)
        
        for _ in range(num_sentences):
            pattern = random.choice([
                f"{random.choice(subjects)} {random.choice(verbs)} that {random.choice(topics)} are {random.choice(descriptors)}, {random.choice(consequences)}.",
                f"according to {random.choice(subjects)}, {random.choice(topics)} have shown {random.choice(descriptors)} changes, {random.choice(consequences)}.",
                f"the {random.choice(descriptors)} nature of {random.choice(topics)} {random.choice(verbs)} {random.choice(consequences)}.",
                f"researchers studying {random.choice(topics)} have found {random.choice(descriptors)} evidence {random.choice(consequences)}."
            ])
            sentences.append(pattern.lower())
        
        paragraphs.append(" ".join(sentences))
    
    return "\n\n".join(paragraphs)

# Function to generate a random date in the specified range (keeps original case)
def random_date():
    start_date = datetime(2019, 9, 1)
    end_date = datetime(2020, 4, 1)
    random_date = start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds()))
    )
    return random_date.strftime("%Y-%m-%dT%H:%M:%SZ")

# Function to generate author (with 25% chance of being empty, lowercase)
def generate_author():
    if random.random() < 0.25:
        return {"S": ""}
    first_names = ['john', 'jane', 'alex', 'sam', 'michael', 'sarah', 'david', 'emma', 
                  'james', 'linda', 'robert', 'patricia', 'daniel', 'elizabeth']
    last_names = ['smith', 'doe', 'johnson', 'brown', 'davis', 'miller', 'wilson', 
                 'moore', 'taylor', 'anderson', 'thomas', 'jackson', 'white']
    return {"S": f"{random.choice(first_names)} {random.choice(last_names)}"}

# Function to generate a random URI string (lowercase)
def generate_uri():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"uri-{random_string}"

# Updated claims structure (lowercase)
broadClaims = {
    "gw_not_happening": "global warming is not happening",
    "not_caused_by_human": "climate change is not caused by human activities",
    "impacts_not_bad": "climate change impacts are not that bad",
    "solutions_wont_work": "climate solutions won't work",
    "science_movement_unrel": "climate science or movement is unreliable",
    "individual_action": "individual action is pointless"
}

subClaims = {
    "sc_cold_event_denial": "cold weather event disproves global warming",
    "sc_deny_extreme_weather": "extreme weather events are not increasing",
    "sc_natural_variations": "climate change is due to natural variations",
    "sc_past_climate_reference": "past climate changes prove current changes are natural",
    "sc_species_adapt": "species can adapt to climate change",
    "sc_downplay_warming": "warming is not as bad as predicted",
    "sc_policies_negative": "climate policies have negative consequences",
    "sc_policies_ineffective": "climate policies are ineffective",
    "sc_policies_difficult": "climate policies are too difficult to implement",
    "sc_low_support_policies": "there is low public support for climate policies",
    "sc_clean_energy_unreliable": "clean energy sources are unreliable",
    "sc_climate_science_unrel": "climate science is unreliable",
    "sc_no_consensus": "there is no scientific consensus on climate change",
    "sc_movement_unreliable": "the climate movement is unreliable",
    "sc_hoax_conspiracy": "climate change is a hoax or conspiracy"
}

# Mapping between broad claims and subclaims (unchanged)
claim_mapping = {
    "gw_not_happening": ["sc_cold_event_denial", "sc_deny_extreme_weather"],
    "not_caused_by_human": ["sc_natural_variations", "sc_past_climate_reference"],
    "impacts_not_bad": ["sc_species_adapt", "sc_downplay_warming"],
    "solutions_wont_work": ["sc_policies_negative", "sc_policies_ineffective", "sc_policies_difficult", "sc_low_support_policies", "sc_clean_energy_unreliable"],
    "science_movement_unrel": ["sc_climate_science_unrel", "sc_no_consensus", "sc_movement_unreliable", "sc_hoax_conspiracy"],
    "individual_action": []
}

# Updated function to generate a random news article (lowercase except for date)
def generate_article(article_id):
    source = random.choice(sources)
    article = {
        "articleid": {"N": str(article_id)},
        "title": {"S": random_title()},
        "datetime": {"S": random_date()},  # Keeps original case
        "authors": generate_author(),
        "image": {"S": f"https://{source}/images/climate-{random.randint(1000, 9999)}.jpg"},
        "body": {"S": generate_body()},
        "source": {"S": source},
        "url": {"S": f"https://{source}/article-{random.randint(10000, 99999)}"},
        "uri": {"S": generate_uri()},
        "isduplicate": {"BOOL": random.random() < 0.05},  # 5% chance of being a duplicate
        "broadclaims": {"M": {}},
        "subclaims": {"M": {}}
    }

    # Ensure at least one broad claim is selected
    num_broad_claims = random.randint(1, len(broadClaims))
    selected_broad_claims = random.sample(list(broadClaims.keys()), num_broad_claims)

    print(f"selected broad claims: {selected_broad_claims}")  # Debug print (lowercase)

    for bc in selected_broad_claims:
        article["broadclaims"]["M"][bc] = {"S": random_sentence()}
        print(f"added broad claim: {bc}")  # Debug print (lowercase)
        
        # Ensure at least one subclaim is selected if available
        available_subclaims = claim_mapping[bc]
        if available_subclaims:
            num_subclaims = random.randint(1, min(3, len(available_subclaims)))
            selected_subclaims = random.sample(available_subclaims, num_subclaims)
            
            print(f"selected subclaims for {bc}: {selected_subclaims}")  # Debug print (lowercase)

            for sc in selected_subclaims:
                article["subclaims"]["M"][sc] = {"S": random_sentence()}
                print(f"added subclaim: {sc}")  # Debug print (lowercase)

    # Add think tank reference with 30% probability
    if random.random() < 0.3:
        article["think_tank_ref"] = {"S": random_sentence()}
        print("added think tank reference")  # Debug print (lowercase)

    return article

# Generate 500 articles
articles = [generate_article(i) for i in range(500)]

# Save to JSON file
with open('climate_news_data.json', 'w') as f:
    json.dump(articles, f, indent=2)

print("generated 500 articles and saved to climate_news_data.json")

# Print a sample article to verify the structure
print("\nsample article structure:")
print(json.dumps(articles[0], indent=2))

# Print summary of claims in the first 5 articles
for i in range(5):
    print(f"\narticle {i} claims:")
    print(f"broad claims: {list(articles[i]['broadclaims']['M'].keys())}")
    print(f"subclaims: {list(articles[i]['subclaims']['M'].keys())}")