class Packet:
    def __init__(self, pid, transmission_time, priority):
        self.id = pid
        self.transmission_time = transmission_time
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

class PacketHeap:
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

    def insert(self, packet):
        self.heap.append(packet)
        self._bubble_up(len(self.heap) - 1)

    def remove(self):
        if not self.heap:
            return None
        top = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._bubble_down(0)
        return top

    def update_priority(self, pid, new_priority):
        for i, packet in enumerate(self.heap):
            if packet.id == pid:
                old_priority = packet.priority
                packet.priority = new_priority
                if new_priority < old_priority:
                    self._bubble_up(i)
                else:
                    self._bubble_down(i)
                break

# Exemplo de uso:
if __name__ == "__main__":
    router = PacketHeap()
    # Inserindo pacotes: (ID, tempo de transmissão, prioridade)
    router.insert(Packet(101, 10, 3))
    router.insert(Packet(102, 5, 2))
    router.insert(Packet(103, 15, 1))
    
    # Remove e transmite o pacote de maior prioridade
    packet = router.remove()
    print(f"Transmitindo pacote: ID {packet.id}, Tempo {packet.transmission_time}, Prioridade {packet.priority}")
    
    # Atualiza a prioridade de um pacote existente
    router.update_priority(101, 0)
    
    packet = router.remove()
    print(f"Transmitindo pacote: ID {packet.id}, Tempo {packet.transmission_time}, Prioridade {packet.priority}")
