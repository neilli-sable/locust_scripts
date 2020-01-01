from locust import HttpLocust, TaskSet, task, between
import json
import time

headers = {'content-type': 'application/json'}


class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.logout()

    def login(self):
        self.client.post("/login", data=json.dumps(
            {"loginId": "user-id", "password": "user-pass"}), headers=headers)

    def logout(self):
        self.client.post("/logout")

    @task(1)
    def home(self):
        self.client.get("/")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 5000
