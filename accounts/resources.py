from import_export import resources
from accounts.models import Scholarship
 
class MemberResource(resources.ModelResource):
    class Meta:
        model = Scholarship