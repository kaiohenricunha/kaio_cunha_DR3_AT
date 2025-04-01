class Process:
    def __init__(self, pid, exec_time, priority):
        self.id = pid
        self.exec_time = exec_time
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

class ProcessHeap:
    def __init__(self):
        self.heap = []

    def _bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def _bubble_down(self, index):
        n = len(self.heap)
        while 2 * index + 1 < n:
            left = 2 * index + 1
            right = left + 1
            smallest = index
            if self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    def add_process(self, process):
        self.heap.append(process)
        self._bubble_up(len(self.heap) - 1)

    def pop_process(self):
        if not self.heap:
            return None
        top = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._bubble_down(0)
        return top

    def update_priority(self, pid, new_priority):
        for i, process in enumerate(self.heap):
            if process.id == pid:
                old_priority = process.priority
                process.priority = new_priority
                if new_priority < old_priority:
                    self._bubble_up(i)
                else:
                    self._bubble_down(i)
                break

# Exemplo de uso:
if __name__ == "__main__":
    scheduler = ProcessHeap()
    # Adiciona alguns processos: (ID, tempo de execução, prioridade)
    scheduler.add_process(Process(1, 5, 3))
    scheduler.add_process(Process(2, 3, 1))
    scheduler.add_process(Process(3, 2, 2))
    
    # Executa o processo com maior prioridade (menor número)
    proc = scheduler.pop_process()
    print(f"Executando processo: ID {proc.id}, Tempo {proc.exec_time}, Prioridade {proc.priority}")
    
    # Altera a prioridade do processo com ID 3
    scheduler.update_priority(3, 0)
    
    # Executa o próximo processo
    proc = scheduler.pop_process()
    print(f"Executando processo: ID {proc.id}, Tempo {proc.exec_time}, Prioridade {proc.priority}")
