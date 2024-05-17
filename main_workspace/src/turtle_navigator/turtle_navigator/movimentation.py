import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Kill, Spawn, SetPen
import time

class TurtleNavigator(Node):

    def __init__(self):
        super().__init__('turtle_navigator')
        self.publisher = self.create_publisher(
            msg_type=Twist,
            topic='/turtle1/cmd_vel',
            qos_profile=10
        )

    def pubblish_route(self, angular_z, linear_x):
        msg = Twist()
        msg.angular.z = angular_z
        msg.linear.x = linear_x
        self.publisher.publish(msg)

def make_route(publisher):

    caminho = [(0.0, 0.0),
               (2.2, 0.0),
               (0.0, 3.0),
               (2.1, 0.0),
               (0.0, 3.0),
               (2.071, 0.0),
               (0.0, 2.97),
               (0.0, 0.0)]
    
    for angular_z, linear_x in caminho:
        publisher.pubblish_drawing(angular_z, linear_x)
        time.sleep(1)   

def main():
    rclpy.init()
    service_node = rclpy.create_node('service_node')

    # Muda cor do tracejado do caminho percorrido pela tartaruga
    color_client = service_node.create_client(SetPen, '/turtle1/set_pen')
    color_request = SetPen.Request(r=220, g=220, b=0, width=6, off=0)
    async_color_request = color_client.call_async(color_request)
    rclpy.spin_until_future_complete(service_node, async_color_request)

    # Inicia a rota da tartaruga
    publisher = TurtleNavigator()
    make_route(publisher)
    publisher.destroy_node()

    # Mata tartaruga atual
    kill_client = service_node.create_client(Kill, 'kill')
    kill_request = Kill.Request()
    kill_request.name = 'turtle1'
    async_kill_request = kill_client.call_async(kill_request)
    rclpy.spin_until_future_complete(service_node, async_kill_request)
    
    # Cria nova tartaruga com nome 'turtle1'
    spawn_client = service_node.create_client(Spawn, 'spawn')
    spawn_request = Spawn.Request(x = 5.544445, y = 5.544445, theta = 0.0, name='turtle1')
    async_spawn_request = spawn_client.call_async(spawn_request)
    rclpy.spin_until_future_complete(service_node, async_spawn_request)

    # Destroi o nó
    service_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()



