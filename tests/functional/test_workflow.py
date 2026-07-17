"""
Module:
    test_workflow.py

Purpose:
    Functional end-to-end workflow tests.

Coverage:
    - Home page
    - Create task
    - Reject empty task
    - Complete invalid task
    - Delete invalid task

Author:
    Julio Soto
"""


class TestWorkflow:
    """Functional tests for the complete application workflow."""

    def test_complete_user_workflow(self, client):
        """
        Simulate a basic user workflow.
        """

        # Open application
        response = client.get("/")
        assert response.status_code == 200

        # Create a task
        response = client.post(
            "/add",
            data={
                "title": "Functional Test",
                "description": "Testing complete workflow",
            },
        )

        assert response.status_code == 302

        # Reject invalid task
        response = client.post(
            "/add",
            data={
                "title": "",
                "description": "Should not be created",
            },
        )

        assert response.status_code == 302

        # Invalid complete request
        response = client.post("/complete/invalid-id")

        assert response.status_code == 302

        # Invalid delete request
        response = client.post("/delete/invalid-id")

        assert response.status_code == 302

        # Return to home
        response = client.get("/")

        assert response.status_code == 200
