import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory, APISimpleTestCase, APITestCase, force_authenticate

from .models import TODO, Project
from .views import ProjectModelViewSet, TODOModelViewSet

User = get_user_model()


class TestProjectModelViewSet(TestCase):
    def test_get_project_list(self):
        factory = APIRequestFactory()
        request = factory.get("/api/projects/")
        view = ProjectModelViewSet.as_view({"get": "list"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_TODO_list(self):
        factory = APIRequestFactory()
        request = factory.get("/api/TODO/")
        view = TODOModelViewSet.as_view({"get": "list"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_project(self):
        factory = APIRequestFactory()
        data = {"name": "Project Test", "repo_link": "http://localhost", "users": []}
        request = factory.post("/api/projects/", data=data, format="json")
        view = ProjectModelViewSet.as_view({"post": "create"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_project_with_auth(self):
        factory = APIRequestFactory()

        admin = User.objects.create_superuser("admin", "admin@local.host", "password")
        admin_uuid = admin.uuid

        data = {
            "name": "Project Test",
            "repo_link": "http://localhost",
            "users": [admin_uuid],
        }
        request = factory.post("/api/projects/", data=data, format="json")

        force_authenticate(request, admin)
        view = ProjectModelViewSet.as_view({"post": "create"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestTODOViewSet(APITestCase):
    def test_get_TODO_list(self):
        response = self.client.get("/api/TODO/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        admin = User.objects.create_superuser("admin", "admin@local.host", "password")
        self.client.login(username="admin", password="password")
        response = self.client.get("/api/TODO/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_TODO(self):
        user = User.objects.create(email="user@local.host", username="user", password="password")
        project = Project.objects.create(name="Project Test", repo_link="http://localhost")
        project.users.add(user)

        todo = TODO.objects.create(project=project, created_by=user, task_text="test text")
        admin = User.objects.create_superuser("admin", "admin@local.host", "password")
        self.client.login(username="admin", password="password")

        response = self.client.put(
            f"/api/TODO/{todo.uuid}/",
            {"project": project.uuid, "created_by": user.uuid, "task_text": "NEW TEXT"},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        todo = TODO.objects.get(uuid=todo.uuid)
        self.assertEqual(todo.task_text, "NEW TEXT")

        self.client.logout

    def test_edit_TODO_mixer(self):
        todo = mixer.blend(TODO)

        admin = User.objects.create_superuser("admin", "admin@local.host", "password")
        self.client.login(username="admin", password="password")

        response = self.client.put(
            f"/api/TODO/{todo.uuid}/",
            {
                "project": todo.project.uuid,
                "created_by": todo.created_by.uuid,
                "task_text": "NEW TEXT",
            },
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        todo = TODO.objects.get(uuid=todo.uuid)
        self.assertEqual(todo.task_text, "NEW TEXT")

        self.client.logout
