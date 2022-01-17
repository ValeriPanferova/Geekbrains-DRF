from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.response import Response

from .models import Project, TODO
from .serializers import ProjectModelSerializer, TODOModelSerializer
from .filters import ProjectFilter, TODOFilter


class ProjectPageNumberPagination(PageNumberPagination):
    page_size = 10


class TODOPageNumberPagination(PageNumberPagination):
    page_size = 20


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectPageNumberPagination
    filterset_class = ProjectFilter


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
    pagination_class = TODOPageNumberPagination
    filterset_class = TODOFilter

    def destroy(self, request, *args, **kwargs):
        todo = self.get_object()
        todo.is_active = False
        todo.save()
        return Response(status=status.HTTP_200_OK)
