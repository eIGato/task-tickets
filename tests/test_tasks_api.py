import pytest
from django.urls import reverse
from tasks.models import Task, Comment


@pytest.mark.django_db
def test_create_task(auth_client, user):
    url = reverse("task-list")
    payload = {
        "title": "Test task",
        "description": "Do something",
    }
    response = auth_client.post(url, payload, format="json")
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test task"
    assert data["created_by"]["id"] == user.id
    assert data["status"] == "todo"


@pytest.mark.django_db
def test_assign_task(auth_client, user, another_user):
    url = reverse("task-list")
    payload = {
        "title": "Assignable task",
        "assignee": another_user.id,
    }
    response = auth_client.post(url, payload, format="json")
    assert response.status_code == 201
    task_id = response.json()["id"]

    task = Task.objects.get(id=task_id)
    assert task.assignee == another_user


@pytest.mark.django_db
def test_complete_task(auth_client, user):
    task = Task.objects.create(title="To complete", created_by=user)
    url = reverse("task-complete", kwargs={"pk": task.id})

    response = auth_client.post(url)
    assert response.status_code == 200
    task.refresh_from_db()
    assert task.status == task.Status.DONE


@pytest.mark.django_db
def test_comment_task(auth_client, user):
    task = Task.objects.create(title="With comments", created_by=user)
    url = reverse("comment-list")
    payload = {"task": task.id, "text": "First comment"}

    response = auth_client.post(url, payload, format="json")
    assert response.status_code == 201
    data = response.json()
    assert data["task"] == task.id
    assert data["author"]["id"] == user.id

    assert Comment.objects.filter(task=task).count() == 1


@pytest.mark.django_db
def test_get_users_list(auth_client, user, another_user):
    url = reverse("user-list")
    response = auth_client.get(url)

    assert response.status_code == 200
    data = response.json()
    ids = {u["id"] for u in data}

    assert user.id in ids
    assert another_user.id in ids
