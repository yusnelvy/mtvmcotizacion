from haystack import indexes
from direccion.models import Pais


class PaisIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    #model fields
    pais = indexes.CharField(model_attr='pais')

    def get_model(self):
        return Pais
