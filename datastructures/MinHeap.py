class MinHeap:

    def __init__(self):
        self.array = []
        self.pos = []
        self.size = 0

    @staticmethod
    def new_min_heap_node(v, dist):
        return [v, dist]

    def swap_min_heap_node(self, a, b):
        t = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = t

    def min_heapify(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < self.size and self.array[left][1] < \
                self.array[smallest][1]:
            smallest = left

        if right < self.size and self.array[right][1] < \
                self.array[smallest][1]:
            smallest = right

        if smallest != idx:
            self.pos[self.array[smallest][0]] = idx
            self.pos[self.array[idx][0]] = smallest
            self.swap_min_heap_node(smallest, idx)
            self.min_heapify(smallest)

    def extract_min(self):
        if self.is_empty():
            return

        root = self.array[0]

        last_node = self.array[self.size - 1]
        self.array[0] = last_node
        self.pos[last_node[0]] = 0
        self.pos[root[0]] = self.size - 1
        self.size -= 1
        self.min_heapify(0)

        return root

    def is_empty(self):
        return True if self.size == 0 else False

    def decrease_key(self, v, dist):
        i = self.pos[v]
        self.array[i][1] = dist

        while i > 0 and self.array[i][1] < self.array[(i - 1) // 2][1]:
            self.pos[self.array[i][0]] = (i - 1) / 2
            self.pos[self.array[(i - 1) // 2][0]] = i
            self.swap_min_heap_node(i, (i - 1) // 2)

            i = (i - 1) // 2

    def is_in_minheap(self, v):
        if self.pos[v] < self.size:
            return True
        return False


def print_array(parent, n, key):
    print("Edges -- Minimum Cost Forest")
    for i in range(1, n):
        if key[i] != 9000000000:
            print("[%d]--[%d] weight: %d" % (parent[i], i, key[i]))

