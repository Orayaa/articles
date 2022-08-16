from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

articles = [] 

for i in range(10) : 
    #Read TXT file  C:\Users\ADMIN\Desktop\6206021610081 
    f = open(f"wiki_article_{i}.txt", "r") 
    article = f.read() 
    # Tokenize the article: tokens 
    tokens = word_tokenize(article) 
    # Convert the tokens into lowercase: lower_tokens 
    lower_tokens = [t.lower() for t in tokens] 
    # Retain alphabetic words: alpha_only 
    alpha_only = [t for t in lower_tokens if t.isalpha()] 
    # Remove all stop words: no_stops 
    no_stops = [t for t in alpha_only if t not in stopwords.words('english')] 
    # Instantiate the WordNetLemmatizer 
    wordnet_lemmatizer = WordNetLemmatizer() 
    # Lemmatize all tokens into a new list: lemmatized 
    lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops] 
    #list_article 
    articles.append(lemmatized) 

print(articles[0]) 
# Shophee