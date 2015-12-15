from import_export import resources
from mueble.models import Mueble


class MuebleResource(resources.ModelResource):

    class Meta:
        model = Mueble
