# -*- coding: utf-8 -*-
"""1.MaxHeap

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nTqc8J0VV6qhfYcasCGt9dnQBBHL_spl
"""

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete(self, value):
        try:
            idx = self.heap.index(value)
        except ValueError:
            return

        self.heap[idx] = self.heap[-1]
        self.heap.pop()

        if idx < len(self.heap):
            self._heapify_down(idx)

    def get_max(self):
        if self.heap:
            return self.heap[0]
        else:
            return None

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
                largest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
                largest = right_child_index

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

if __name__ == "__main__":
    heap = MaxHeap()
    while True:
        print("\nChoose an operation:")
        print("1. Insert")
        print("2. Delete")
        print("3. Get Max")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            value = int(input("Enter value to insert: "))
            heap.insert(value)
            print(f"{value} inserted into heap.")
            print("Current heap:", heap.heap)
        elif choice == '2':
            value = int(input("Enter value to delete: "))
            heap.delete(value)
            print(f"{value} deleted from heap.")
            print("Current heap:", heap.heap)
        elif choice == '3':
            max_element = heap.get_max()
            if max_element is not None:
                print(f"Maximum element in heap: {max_element}")
            else:
                print("Heap is empty.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
