#!/usr/bin/evn/python3
import rospy
from gazebo_msgs.srv import ApplyJointEffort, GetJointProperties

msg_topic = '/gazebo/apply_joint_effort'
joint_left = 'dd_robot::left_wheel_hinge'
joint_right = 'dd_robot::right_wheel_hinge'

msg_topic_feedback = '/gazebo/get_joint_properties'

pub_feedback = rospy.ServiceProxy(msg_topic_feedback, GetJointProperties)
rospy.init_node('dd_ctrl', anonymous=True)
pub = rospy.ServiceProxy(msg_topic, ApplyJointEffort)

effort = 1.0
start_time = rospy.Time(0,0)

f = 0.5
T = 1/f
end_time = rospy.Time(T,0)
rate = rospy.Rate(.5)

while True:
    effort = -effort
    pub(joint_left, effort, start_time, end_time)
    val = pub_feedback(joint_left)
    print(val.position)
    rate.sleep()
