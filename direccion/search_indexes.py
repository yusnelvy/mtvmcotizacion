from haystack import indexes

from direccion.models import Pais, Ciudad


class PaisIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    pais = indexes.CharField(model_attr='pais')

    def get_model(self):
        return Pais

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class CiudadIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    pais = indexes.CharField(model_attr='pais')
    ciudad = indexes.CharField(model_attr='ciudad')
    provincia = indexes.CharField(model_attr='provincia')

    def get_model(self):
        return Ciudad

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
