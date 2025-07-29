from flask import Flask, render_template, request, session
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scraper.defination import get_definition
from trie.trie import Trie
from corrections.edit import get_closest_words

app = Flask(__name__)
app.secret_key = 'kuch_secret_key_jo_session_ke_liye_hai'

# Load words into Trie
trie = Trie()
word_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'words.txt')
word_list = []
with open(word_file, 'r') as f:
    for line in f:
        word = line.strip()
        if word:
            word_list.append(word)
            trie.insert(word)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Hinglish comments: Yeh function homepage handle karta hai
    definition = None
    suggestions = []
    query = ''
    message = ''
    search_history = session.get('search_history', [])

    if request.method == 'POST':
        query = request.form.get('word', '').strip()
        if query:
            if trie.search(query):
                word_info = get_definition(query)
                message = f"✅ '{query}' found in dictionary."
            else:
                message = f"❌ '{query}' not found."
                suggestions = trie.starts_with(query)
                if not suggestions:
                    suggestions = get_closest_words(query, word_list)
                if suggestions:
                    word_info = get_definition(suggestions[0])
                    message += f" Did you mean '{suggestions[0]}'? Definition shown below."
                else:
                    word_info = {"error": "No suggestions found."}
            # Update search history
            if query not in search_history:
                search_history.insert(0, query)
                if len(search_history) > 10:
                    search_history.pop()
            session['search_history'] = search_history
            definition = word_info
    return render_template('index.html', definition=definition, suggestions=suggestions, query=query, message=message, search_history=search_history)

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
