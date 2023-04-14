#!/usr/bin/env python
import roslib
import rospy

import tf
from geometry_msgs.msg import TransformStamped
from posedetection_msgs.msg import ObjectDetection

def handle_pose(msg):
    br = tf.TransformBroadcaster()
    if len(msg.objects)==0:
        return
    p = msg.objects[0].pose
    br.sendTransform((p.position.x, p.position.y, p.position.z),
                     (p.orientation.x, p.orientation.y, p.orientation.z, p.orientation.w),
                     msg.header.stamp,
                     "checker_marker_frame",
                     "camera_color_optical_frame")

if __name__ == '__main__':
    rospy.init_node('marker_tf_broadcaster')
    rospy.Subscriber('/checkerdetector/ObjectDetection',
                     ObjectDetection,
                     handle_pose)
    rospy.spin()
