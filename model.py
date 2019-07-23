import pandas as pd
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score #, confusion_matrix
from nltk.corpus import stopwords
import re
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import classification_report
from sklearn.linear_model import SGDClassifier
from sklearn.externals import joblib

df = pd.read_csv('data.csv')
df = df[pd.notnull(df['Flair'])]
df = df[pd.notnull(df['Title'])]

my_tags = ['Non-Political', 'Politics', 'AskIndia', 'Sports','Food','[R]eddiquette','Science/Technology','Business/Finance','Policy/Economy', 'Other']

REPLACE_BY_SPACE_RE = re.compile('[/()@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    if type(text)!=float:
        text = text.lower()
    try:
        text = REPLACE_BY_SPACE_RE.sub(' ', text)
    except:
   		ran=0
    try:
        text = BAD_SYMBOLS_RE.sub('', text) 
    except:
    	ran=0
    if type(text)!=float:
        text = ' '.join(word for word in text.split() if word not in STOPWORDS) 
    if text==" ":
    	text=a
    return text

df['Title'] = df['Title'].apply(clean_text)
X = df.Title
y = df.Flair
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state = 42)

sgd = Pipeline([('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42, max_iter=5, tol=None)),
               ])
sgd.fit(X_train, y_train)

y_pred = sgd.predict(X_test)

print('accuracy %s' % accuracy_score(y_pred, y_test))
print(classification_report(y_test, y_pred,target_names=my_tags))


joblib.dump(sgd,'model.pkl')