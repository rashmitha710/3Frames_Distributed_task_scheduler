##3
workers = set()

def register_worker(worker_id):
    workers.add(worker_id)

def remove_worker(worker_id):
    workers.discard(worker_id)
