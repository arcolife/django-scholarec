# handle user search history
from users.models import History 
from django.utils import timezone
import string
from search import es_query

def add_to_history(query, username):
    #print query, " | ", username
    try:
        s_history = History.objects.get(user_id__contains=username)
        #print "User %s found in DB!\n" % (username)
    except:
        s_history = History( user_id=username, last_search=timezone.now())    
        print "User %s not found in DB. Created one." % (username)
    '''
    # split multi-word query into individual ones'
    for word in query.split():
        if word not in s_history.keywords:
            s_history.keywords.append(word)
    '''
    # append query without splitting multi-word query
    if query not in s_history.keywords:
        s_history.keywords.append(query)
    else:
        s_history.keywords.remove(query)
        s_history.keywords.append(query)
    s_history.save()
    #print "History For username: %s \nKeywords: %s" \
    #    % (username, str(s_history.keywords))
    return s_history.keywords

def add_rating(username, paper_id, rating, query, keyword):
    try:
        s_history = History.objects.get(user_id__contains=username)
    except:
        add_to_history(query, username)
        s_history = History.objects.get(user_id__contains=username)
    #table = string.maketrans("","")
    #keyword = '%20'.join(keyword.translate(table, string.punctuation).split())
    if paper_id not in s_history.fav_papers:
        s_history.fav_papers.append(paper_id)
        s_history.fav_ratings.append(rating)
        s_history.fav_keywords.append(keyword)
        print "%s added to %s's ratings!\n" % (paper_id, username)
    elif paper_id in s_history.fav_papers:
        ix = s_history.fav_papers.index(paper_id) 
        if s_history.fav_ratings[ix] != rating:
            s_history.fav_ratings[ix] = rating
            print "%s's rating changed in %s's ratings!\n" % (paper_id, username)
        else:
            print "%s is already in %s's ratings!\n" % (paper_id, username)
    else:
        print "%s is already in %s's ratings!\n" % (paper_id, username)
    s_history.save()
    return ''

def add_to_collection(username, doc_id, paper_id, title):
    try:
        s_history = History.objects.get(user_id__contains=username)
    except:
        add_to_history(query, username)
        s_history = History.objects.get(user_id__contains=username)
    if doc_id not in s_history.collection:
        #s_history.collection.append(doc_id)
        s_history.collection[doc_id] = [title, paper_id]
        print "%s added to %s's collection!\n" % (doc_id, username)
    else:
        print "%s is already in %s's collection!\n" % (doc_id, username)
    s_history.save()
    return ''
    
def remove_from_collection(username, doc_id):
    try:
        s_history = History.objects.get(user_id__contains=username)
    except:
        add_to_history(query, username)
        s_history = History.objects.get(user_id__contains=username)
    if doc_id in s_history.collection:        
        #s_history.collection.remove(doc_id)
        s_history.collection.pop(doc_id)
        print "%s removed from %s's collection!\n" % (doc_id, username)
    else:
        print "%s isn't already present in %s's collection!\n" % (doc_id, username)
    s_history.save()
    return ''
        
def get_ratings(username):
    try:
        s_history = History.objects.get(user_id__contains=username)
        return s_history.fav_papers, s_history.fav_ratings, s_history.fav_keywords
    except:
        s_history = History( user_id=username, last_search=timezone.now())
        s_history.save()
        print "User %s not found in DB. Created one." % (username)    
        return [],[],[]

def get_collection(username):
    try:
        s_history = History.objects.get(user_id__contains=username)
        return s_history.collection
    except:
        s_history = History( user_id=username, last_search=timezone.now())
        s_history.save()
        print "User %s not found in DB. Created one." % (username)    
        return []

def get_recommendations(username):
    try:
        s_history = History.objects.get(user_id__contains=username)
        topics = s_history.fav_keywords
    except:
        s_history = History( user_id=username, last_search=timezone.now())
        s_history.save()
        print "User %s not found in DB. Created one." % (username)    
        return [], []
    recos = []
    try:
        print "favorited: ", topics
        for fav in set(topics):
            temp = es_query.__run_query(fav, search_size=1, fields='title,ID')
            recos.append(temp['hits']['hits'][0]['fields'])
        if len(recos) > 3:
            return recos[:3], list(set(topics))
        else:
            return recos, list(set(topics))
    except:
        return [], []
