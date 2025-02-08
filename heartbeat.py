import time
import requests

def send_heartbeat(worker_id):
    while True:
        requests.post("http://scheduler/heartbeat", json={"worker_id": worker_id})
        time.sleep(5)

def recover_failed_tasks():
    failed_tasks = redis_client.smembers("failed_tasks")
    for task in failed_tasks:
        redis_client.lpush("task_queue", task)  # Reassign task
