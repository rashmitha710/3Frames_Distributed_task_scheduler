import redis
import json

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def add_task(task_id, task_data):
    task = {"task_id": task_id, "data": task_data, "status": "pending"}
    redis_client.lpush("task_queue", json.dumps(task))

def fetch_task():
    task = redis_client.rpop("task_queue")
    return json.loads(task) if task else None


