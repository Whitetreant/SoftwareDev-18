from tastypie.resources import ModelResource
from api.models import Note,temp
from tastypie.authorization import Authorization

class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        queryset2 = temp.objects.all()
        resource_name= 'Type'
        authorization = Authorization()
        fields = ['Value','created_at']
# Create your views here.
