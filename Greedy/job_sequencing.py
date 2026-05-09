class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit


def job_sequencing(jobs):
    jobs.sort(key=lambda x: x.profit, reverse=True)

    max_deadline = max(job.deadline for job in jobs)

    slots = [False] * max_deadline
    result = []

    for job in jobs:
        for j in range(job.deadline - 1, -1, -1):
            if not slots[j]:
                slots[j] = True
                result.append(job.job_id)
                break

    return result


jobs = [
    Job('A',2,100),
    Job('B',1,19),
    Job('C',2,27),
    Job('D',1,25),
    Job('E',3,15)
]

print(job_sequencing(jobs))