import datetime
from haystack import indexes
from search.models import Note

'''
# post.search_indexes
import search
from search.core import porter_stemmer
from post.models import Post

# index used to retrieve posts using the title, content or the
# category.
search.register(Post, ('title', 'content','category', ),
    indexer=porter_stemmer)

'''

class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='user')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Note

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
