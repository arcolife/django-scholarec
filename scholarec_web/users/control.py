# handle user search history
from users.models import History 
from django.utils import timezone

def add_to_history(query, username):
    #print query, " | ", username
    try:
        s_history = History.objects.get(user_id__contains=username)        
    except:
        s_history = History( user_id=username, last_search=timezone.now())    
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
