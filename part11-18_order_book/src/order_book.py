# Write your solution here:
class Task:
    id_global = 1

    def __init__(self, description, programmer,workload):
        self.description = description
        self.workload = workload
        self.programmer = programmer
        self.status = False
        self.id = Task.id_global
        Task.id_global += 1

    def is_finished(self):
        return self.status
    
    def mark_finished(self):
        self.status = True

    def __str__(self):
        if self.is_finished():
            status = 'FINISHED'
        else:
            status = 'NOT FINISHED'
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"


class OrderBook:
    def __init__(self) -> None:
        self.orders = []

    def add_order(self, description, programmer,workload):
        task = Task(description, programmer,workload)
        self.orders.append(task)

    def all_orders(self):
        return self.orders
    
    def programmers(self):
        result = []
        for task in self.orders:
            result.append(task.programmer)
        return list(set(result))
    
    def mark_finished(self, id: int):
        for task in self.all_orders():
            if task.id == id:
                task.status = True
                return
        raise ValueError("Not found")
        


    def finished_orders(self):
        result = []
        for task in self.orders:
            if task.is_finished():
                result.append(task)
        return result

    def unfinished_orders(self):
        result = []
        for task in self.orders:
            if not task.is_finished():
                result.append(task)
        return result