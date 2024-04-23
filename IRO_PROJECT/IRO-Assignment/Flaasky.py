from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import numpy as np
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.metrics import edit_distance
import string

app = Flask(__name__)

# Ensure necessary NLTK downloads
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Load the scraped data
with open('scraped_data.json', 'r') as f:
    scraped_data = json.load(f)

# Extract the text content for TF-IDF vectorization
document_texts = [item['content'] for item in scraped_data]

# Create a TF-IDF vectorizer and fit it to the document texts
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(document_texts)
feature_names = vectorizer.get_feature_names_out()

def correct_spelling(word):
    # Find the closest word in terms of edit distance from a larger dictionary
    lexicon = set(feature_names)
    closest_word = min(lexicon, key=lambda x: edit_distance(word, x))
    return closest_word if closest_word in lexicon else word

def expand_query(query):
    expanded_query = []
    for token in word_tokenize(query):
        # Find synonyms or related terms using WordNet
        synsets = wordnet.synsets(token)
        if synsets:
            synonyms = set()
            for synset in synsets:
                for lemma in synset.lemmas():
                    synonyms.add(lemma.name())
            expanded_query.extend(synonyms)
        else:
            expanded_query.append(token)
    return ' '.join(expanded_query)

def extract_snippet(content, query):
    # Find the index of the query term in the content
    query_index = content.lower().find(query.lower())
    if query_index == -1:
        return content[:200]  # Return the first 200 characters if the query term is not found
    start_index = max(0, query_index - 100)  # Start 100 characters before the query term
    end_index = min(len(content), query_index + len(query) + 100)  # End 100 characters after the query term
    return content[start_index:end_index]

def validate_query(query_text):
    # Check if the query contains only whitespace
    if not query_text.strip():
        return False, "Please enter a search query."
    
    # Check if the query contains only alphabets, numbers, and spaces
    if not query_text.replace(' ', '').isalnum():
        return False, "Query should only contain alphabets, numbers, and spaces."
    
    # Check if the query is not too short
    if len(query_text.strip()) < 3:
        return False, "Query should be at least 3 characters long."
    
    # Check if the query does not consist only of stopwords
    query_words = word_tokenize(query_text.lower())
    if all(word in stopwords.words('english') for word in query_words):
        return False, "Query should contain meaningful words."
    
    # Check if the query does not contain special characters except for spaces
    if any(char in string.punctuation for char in query_text.strip()) and not all(char.isspace() or char in string.punctuation for char in query_text.strip()):
        return False, "Query should not contain special characters except for spaces."
    
    # Check if the query is not excessively long
    if len(query_text.strip()) > 100:
        return False, "Query is too long. Please provide a shorter query."
    
    # Additional validation logic can be added here
    return True, None

@app.route('/')
def index():
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search():
    query_text = request.form['query']

    # Validate the search query
    is_valid, error_message = validate_query(query_text)
    if not is_valid:
        # Redirect back to the search page with an error
        return render_template('search.html', error=error_message)

    # Correct spelling in the query
    corrected_query = ' '.join(correct_spelling(word) for word in query_text.split())

    # Expand the query using WordNet
    expanded_query = expand_query(corrected_query)

    # Preprocess the expanded query text and vectorize it
    query_vector = vectorizer.transform([expanded_query])

    # Calculate cosine similarity between the query vector and the document tf-idf matrix
    similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()

    # Rank documents by similarity score
    top_indices = np.argsort(similarities)[-10:][::-1]  # Get the indices of the top 10 results

    # Collect the top results
    results = [
        {
            'url': scraped_data[idx]['url'],  # Assuming 'url' is a field in your scraped data
            'title': scraped_data[idx]['title'],  # Assuming 'title' is a field in your scraped data
            'score': float(similarities[idx]),
            'excerpt': extract_snippet(scraped_data[idx]['content'], corrected_query)
        } for idx in top_indices if similarities[idx] > 0
    ]

    # Render the results page with the search results
    return render_template('results.html', query=corrected_query, results=results, original_query=query_text)

if __name__ == '__main__':
    app.run(debug=True)
