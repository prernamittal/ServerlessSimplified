# Serverless Platform from Scratch

**1. Aim and Description:**
The aim of this project is to implement a simplified serverless platform using distributed systems concepts. The project simulates a serverless environment where requests are routed to multiple nodes for processing. It demonstrates load balancing, fault tolerance, and queuing mechanisms commonly found in distributed systems.

**2. Use Cases:**
- Scalable web applications
- Real-time data processing systems
- Serverless architecture

**3. GUI:**
The project includes a graphical user interface (GUI) built using PyQt6. The GUI displays real-time logs of request processing, node health, CPU and memory usage, and queue status.

**4. Files Explanation:**
- `serverlessApp.py`: Main application file containing the implementation of the serverless platform and GUI.
- `loadBalancer.py`: Module implementing the load balancing logic.
- `serverless.log`: Log file capturing system events and metrics.

**5. How to Run:**
Follow these steps to run the project:
1. Ensure Python 3 and PyQt6 are installed on your system.
2. Clone the repository or download the project files.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the following command to execute the application:
   ```
   python serverlessApp.py
   ```
5. The GUI window will open, allowing interaction with the serverless platform.

**6. Similarities to Serverless Platform and Distributed Systems concepts:**
- **Dynamic Resource Allocation:** Nodes (representing serverless instances) are created and removed dynamically based on demand. This allows for efficient resource allocation, scaling up or down as needed without requiring manual intervention.

- **Load Balancing:** The LoadBalancer class distributes incoming requests among available nodes. This ensures that the workload is evenly distributed across the serverless instances, optimizing performance and resource utilization.

- **Fault Tolerance and Recovery:** The system handles node failures gracefully. When a node fails, it is removed from the pool of available nodes, and a new node may be added to replace it. This demonstrates resilience to failures, ensuring that the system continues to operate despite individual node failures.

- **Scalability:** The system can scale horizontally by adding more nodes to handle increased demand. This allows the system to accommodate varying workloads without compromising performance or reliability.

- **Event-Driven Model:** The system processes requests asynchronously in response to events. Each request triggers the execution of a function (represented by a node), allowing the system to respond dynamically to incoming requests.

- **Logging and Monitoring:** The code integrates logging and monitoring functionalities using the logging module and psutil library. This allows monitoring system performance metrics such as CPU usage, memory usage, and node health. Logging enables administrators to track system behavior and diagnose issues, while monitoring provides insights into the overall health and performance of the distributed system.

- **Message Passing:** Requests in the queue represent messages passed between components of the distributed system. The queuing system serves as a message broker, facilitating communication between clients and nodes in the serverless platform. Messages are enqueued, dequeued, and processed according to predefined algorithms, ensuring reliable message passing and coordination within the distributed system.

