"""
Module:
    test_routes.py

Purpose:
    Integration tests for Flask routes.

Coverage:
    - Home page
    - Add task
    - Complete task
    - Delete task
"""

# from models.task import Task


class TestRoutes:

    def test_home_page(self, client):
        response = client.get("/")

        assert response.status_code == 200

    def test_add_task(self, client):
        response = client.post(
            "/add",
            data={
                "title": "Learn Flask",
                "description": "Integration test",
            },
        )

        assert response.status_code == 302

    def test_add_task_without_title(self, client):
        response = client.post(
            "/add",
            data={
                "title": "",
                "description": "Should fail",
            },
        )

        assert response.status_code == 302

    def test_complete_invalid_task(self, client):
        response = client.post("/complete/invalid-id")

        assert response.status_code == 302

    def test_delete_invalid_task(self, client):
        response = client.post("/delete/invalid-id")

        assert response.status_code == 302
