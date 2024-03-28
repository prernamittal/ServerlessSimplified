import sys, logging, os
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit
from PyQt6.QtCore import QTimer
import random
import psutil  
from loadBalancer import LoadBalancer
from collections import deque

if os.path.exists('serverless.log'):
    os.remove('serverless.log')

logging.basicConfig(filename='serverless.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class Node:
    def process_request(self, request):
        logging.info(f"Processing: {request}")
        return f"Processing: {request}"

class ServerlessApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.request_queue = deque()

        self.setWindowTitle("Serverless Platform Simplified")
        self.setGeometry(100, 100, 600, 420)

        self.load_balancer = None
        self.nodes = []
        self.requests = []

        self.init_nodes()
        self.init_ui()

        self.monitor_timer = QTimer()
        self.monitor_timer.timeout.connect(self.monitor_system)
        self.monitor_timer.start(3000)  # Monitor system every 3 seconds

    def init_nodes(self):
        # Create 5 nodes initially
        self.nodes = [Node() for _ in range(5)]

    def init_ui(self):
        # Syntax : window.setGeometry(x, y, width, height)
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(20, 20, 560, 290)

        self.start_button = QPushButton("Start", self)
        self.start_button.setGeometry(50, 360, 100, 30)
        self.start_button.clicked.connect(self.start_simulation)

        self.stop_button = QPushButton("Stop", self)
        self.stop_button.setGeometry(200, 360, 100, 30)
        self.stop_button.clicked.connect(self.stop_simulation)
        self.stop_button.setEnabled(False)

        self.clear_button = QPushButton("Clear", self)
        self.clear_button.setGeometry(350, 360, 100, 30)
        self.clear_button.clicked.connect(self.clear_output)

    def start_simulation(self):
        self.load_balancer = LoadBalancer(self.nodes)
        self.requests = [(f"Request {i}", None) for i in range(20)]
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.timer = QTimer()
        self.timer.timeout.connect(self.process_request)
        self.timer.start(1000)  # Request every second

        # Start a timer to simulate node failures
        self.failure_timer = QTimer()
        self.failure_timer.timeout.connect(self.fail_node)
        self.failure_timer.start(5000)  # Simulate node failure every 5 seconds

    def stop_simulation(self):
        self.timer.stop()
        self.failure_timer.stop()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    def process_request(self):
        if self.requests:
            request, node = self.requests.pop(0)
            if node:
                self.text_edit.append(f"{request} processed by Node {node}")
                logging.info(f"{request} processed")
            else:
                self.request_queue.append(request)  # Enqueue the request
                self.text_edit.append(f"{request} added to the queue")

                node = self.load_balancer.route_request(request)
                self.text_edit.append(f"{request} routed to Node {node}")
                logging.info(f"{request} routed to Node {node}")
                logging.info(f"Queue Size: {len(self.request_queue)}") # Log queue size
                self.text_edit.append(f"{request} processed by Node {node}")
                logging.info(f"{request} processed")

        if self.request_queue:
            request = self.request_queue.popleft()  # Dequeue the request
            self.text_edit.append(f"{request} dequeued from the queue") 
            logging.info(f"Queue Size: {len(self.request_queue)}") # Log queue size 
                        

    def fail_node(self):
        if self.nodes:
            failed_node = random.choice(self.nodes)
            self.text_edit.append(f"Node {failed_node} has failed.")
            self.nodes.remove(failed_node)  # Remove the failed node from the list
            self.nodes.append(Node())  # Add a new node to replace the failed one
            self.text_edit.append(f"New Node {self.nodes[-1]} added to replace the failed node.")
            logging.warning(f"Node {failed_node} has failed.")

    def monitor_system(self):
        # Monitor CPU and memory usage
        cpu_percent = psutil.cpu_percent(interval=None)
        memory_percent = psutil.virtual_memory().percent
        logging.info(f"CPU Usage: {cpu_percent}%  Memory Usage: {memory_percent}%")

        # Monitor node health (simulated by response time)
        for node in self.nodes:
            response_time = random.randint(10, 100)  # Simulate response time between 10ms to 100ms
            logging.info(f"Node {node} Response Time: {response_time}ms")

    def clear_output(self):
        self.text_edit.clear()
        self.queue_edit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServerlessApp()
    window.show()
    sys.exit(app.exec())
