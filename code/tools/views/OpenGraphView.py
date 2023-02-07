from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

class OpenGraphView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tools/open_graph.html'

    def get(self, request):
        # queryset = 
        # self.object = self.get_object()
        return Response({'msg': 'hihi'})
