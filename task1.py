import random
from queue import Queue
from uuid import uuid4


class RequestQueue:
    REQUEST_TYPES = ['name change', 'surname change', 'address change', 'ID change']

    def __init__(self):
        self.queue = Queue()

    def generate_request(self):
        request_type = random.choice(self.REQUEST_TYPES)
        request = {'id': str(uuid4()), 'type': request_type}
        self.queue.put(request)
        print(f"Request {request['id']} for {request['type']} added to queue.")

    def process_request(self):
        if not self.queue.empty():
            request = self.queue.get()
            print(f"Request {request['id']} for {request['type']} has been processed.")
        else:
            print("Queue is empty.")

    def run(self):
        print("Service Center Request Processing System")
        print("Commands:")
        print("  1 or 'generate' - automatically generate new request")
        print("  2 or 'process' - process request from queue")
        print("  3 or 'exit' - quit program")
        print()

        while True:
            command = input("Enter command: ").strip().lower()

            if command in ('3', 'exit'):
                print("Exiting program...")
                break
            elif command in ('1', 'generate'):
                self.generate_request()
            elif command in ('2', 'process'):
                self.process_request()
            else:
                print("Invalid command. Use 1-3 or 'generate', 'process', 'exit'.")


if __name__ == "__main__":
    request_queue = RequestQueue()
    request_queue.run()
