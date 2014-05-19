# handle user search history
from users.models import History 
from django.utils import timezone
import string

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

def add_to_collection(username, paper_id):
    try:
        s_history = History.objects.get(user_id__contains=username)
    except:
        add_to_history(query, username)
        s_history = History.objects.get(user_id__contains=username)
    if paper_id not in s_history.collection:
        s_history.collection.append(paper_id)
        print "%s added to %s's collection!\n" % (paper_id, username)
    else:
        print "%s is already in %s's collection!\n" % (paper_id, username)
    s_history.save()
    return ''
    
def remove_from_collection(username, paper_id):
    try:
        s_history = History.objects.get(user_id__contains=username)
    except:
        add_to_history(query, username)
        s_history = History.objects.get(user_id__contains=username)
    if paper_id in s_history.collection:        
        s_history.collection.remove(paper_id)
        print "%s removed from %s's collection!\n" % (paper_id, username)
    else:
        print "%s isn't already present in %s's collection!\n" % (paper_id, username)
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
