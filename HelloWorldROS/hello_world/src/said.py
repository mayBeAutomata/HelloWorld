## Node to publish a string topic.
#import required libraries
import rospy
from std_msgs.msg import String

# publisher function
def simplePublisher():

    # define publisher object "rospy.Publisher"
    # topic name "topic_1"
    # data type "String"
    # queue size "10"
    simple_publisher = rospy.Publisher('topic_1', String, queue_size = 10)

    # init ros node by "rospy.init_node"
    # topic name "node_1"
    # security level "anonymous"
    rospy.init_node('node_1', anonymous = False)

    # ros publish "rospy.Rate" = 1    
    rate = rospy.Rate(1)
    
    # the string to be published on the topic.
    topic1_content = "Hello World! It's Somto :( ."
    
    while not rospy.is_shutdown():
        # desired string is published using the publish function using the publish object
        simple_publisher.publish(topic1_content)

        # loop at certain rates
        rate.sleep()
        
if __name__== '__main__':
    try:
        simplePublisher()
    except rospy.ROSInterruptException:
        pass