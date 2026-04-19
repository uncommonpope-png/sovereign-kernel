# robotics

Write production-grade robotics software following ROS1/ROS2 patterns and SOLID principles.

## What this skill does
Generates ROS2 nodes, launch files, message definitions, and control algorithms for robotics applications. Also supports hardware-agnostic motion planning and sensor processing.

## ROS2 Python node template
```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class SovereignRobotNode(Node):
    def __init__(self):
        super().__init__('sovereign_robot')
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.sub = self.create_subscription(String, '/soul_command', self.on_command, 10)
        self.timer = self.create_timer(0.1, self.control_loop)
        self.get_logger().info('Sovereign Robot Node started')

    def on_command(self, msg):
        self.get_logger().info(f'Command: {msg.data}')

    def control_loop(self):
        cmd = Twist()
        cmd.linear.x = 0.1   # m/s forward
        cmd.angular.z = 0.0
        self.pub.publish(cmd)

def main():
    rclpy.init()
    node = SovereignRobotNode()
    rclpy.spin(node)
    rclpy.shutdown()
```

## Launch file (ROS2)
```python
from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
    return LaunchDescription([
        Node(package='sovereign_robot', executable='robot_node', name='robot', output='screen')
    ])
```

## PID controller
```python
class PID:
    def __init__(self, kp, ki, kd):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.integral = self.prev_error = 0.0
    def update(self, error, dt):
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        self.prev_error = error
        return self.kp*error + self.ki*self.integral + self.kd*derivative
```

## Sensor processing (LiDAR)
```python
# Process LaserScan message
def process_scan(scan):
    ranges = [r for r in scan.ranges if scan.range_min < r < scan.range_max]
    min_dist = min(ranges) if ranges else float('inf')
    return min_dist
```

## Example commands
```
ACTION: Generate a ROS2 node that subscribes to soul_command topic and controls robot velocity
ACTION: Write a PID controller for line-following robot with P=1.2, I=0.1, D=0.05
```
