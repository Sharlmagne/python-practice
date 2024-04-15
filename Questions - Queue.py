from queue_2 import Queue
import threading
import time

orders = ['pizza','samosa','pasta','biryani','burger']
food_orders = Queue()


def order(orders, queue):
    for order in orders:
        queue.enqueue(order)
        print(order, "Ordered")
        time.sleep(0.5)


def serve(queue):
    time.sleep(1)
    while not queue.is_empty():
        print(queue.dequeue(), "Served")
        time.sleep(2)


# t1 = threading.Thread(target=order, args=(orders, food_orders))
# t2 = threading.Thread(target=serve, args=(food_orders,))
#
# t1.start()
# t2.start()

# Question 2
binary = Queue()
binary.enqueue(1)

binary.enqueue(f"{binary.front()}0")
binary.enqueue(f"{binary.front()}1")




# while not binary.is_empty():
#     print(binary.dequeue())

def produce_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")

    for i in range(n):
        front = numbers_queue.front()
        print("   ", front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")

        numbers_queue.dequeue()


if __name__ == '__main__':
    produce_binary_numbers(10)

