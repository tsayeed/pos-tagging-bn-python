# POS TAGGING FOR BANGLA LANGUAGE

## REQUIREMENTS
- python 3.6
- pipenv

## INSTALLATION
    git clone https://github.com/sayeed910/pos-tagging-bn.git
    cd pos-tagging-bn
    pipenv install
    
## USAGE

- For running the server type
    
    python manage.py runserver
    
- The code for front end resides in the /client/public folder.
- All communications to the server are done via Ajax requests
- To fetch a list of strings an Ajax GET request to this URL is needed
    https://localhost:8000/api/sentences?count=10
- To save the tags of a sentence to the server make a POST request
      https://localhost:8000/api/sentences/<sentence_id>
with the request body
      
    { "word1": 'BISHESHYO', 'WORD2': 'KRIA' ... }
    
    
