import heapq


class PriorityScheduler:
    def __init__(self):
        self.queue = []

    def add_job(self, job_name, priority):
        heapq.heappush(
            self.queue,
            (-priority, job_name)
        )

    def release_job(self):
        if len(self.queue) == 0:
            return None

        priority, job_name = heapq.heappop(self.queue)

        return job_name, -priority

    def size(self):
        return len(self.queue)


print("Activity 6: Priority Scheduler")

scheduler = PriorityScheduler()

scheduler.add_job("Job A", 3)
scheduler.add_job("Job B", 5)
scheduler.add_job("Job C", 1)
scheduler.add_job("Job D", 4)

release_order = []

while scheduler.size() > 0:
    job = scheduler.release_job()
    release_order.append(job[0])

print("Release order:")

for job in release_order:
    print(job)
