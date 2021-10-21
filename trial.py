# -*- coding: UTF-8 -*-
import cv2 as cv
import argparse
import numpy as np
import datetime
import time
from utils import choose_run_mode, load_pretrain_model, set_video_writer
from Pose.pose_visualizer import TfPoseVisualizer
from Action.recognizer import load_action_premodel, framewise_recognize_lstm

parser = argparse.ArgumentParser(description='Action Recognition by OpenPose')
parser.add_argument('--video', help='Path to video file.')
args = parser.parse_args()

# 导入相关模型
estimator = load_pretrain_model('mobilenet_thin')
# action_classifier = load_action_premodel('Action/framewise_openpose_ch1_5_classes.h5')
action_classifier1 = load_action_premodel('Action/LSTM_G.h5')
action_classifier2 = load_action_premodel('Action/LSTM_new_5_class_3.h5')
# action_classifier1 = load_action_premodel('Action/LSTM_A _exp7.h5')
# 参数初始化
realtime_fps = '0.0000'
start_time = time.time()
fps_interval = 1
fps_count = 0
run_timer = 0
frame_count = 0
process_start = 0
elapsed = 0
upper_left = (600, 50)
bottom_right = (1190, 800)
# data_path = './images/abnormal_%01d.jpg'
# 读写视频文件（仅测试过webcam输入）
cap = choose_run_mode(args)
# cap = cv.VideoCapture(data_path,cv.CAP_FFMPEG)
video_writer = set_video_writer(cap, write_fps=int(15.0))
# # 保存关节数据的txt文件，用于训练过程(for training)
f = open('origin_data.txt', 'a+')

while cv.waitKey(1) < 0:
    has_frame, frame = cap.read()
    if has_frame:
        # r = cv.rectangle(frame, upper_left, bottom_right, (100,50,200),5)
        fps_count += 1
        frame_count += 1
        # pose estimation
        process_start = time.time()
        # f = frame[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]]
        humans = estimator.inference(frame)  # show
        # get pose info
        pose = TfPoseVisualizer.draw_pose_rgb(frame, humans)  # return frame, joints, bboxes, xcenter #show
        # recognize the action framewise
        show = framewise_recognize_lstm(pose, action_classifier1, action_classifier2, frame_count)

        height, width = show.shape[:2]
        # 显示实时FPS值
        if (time.time() - start_time) > fps_interval:
            # 计算这个interval过程中的帧数，若interval为1秒，则为FPS
            realtime_fps = fps_count / (time.time() - start_time)
            fps_count = 0  # 帧数清零
            start_time = time.time()
        fps_label = 'FPS:{0:.2f}'.format(realtime_fps)
        cv.putText(show, fps_label, (width - 160, 25), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        # 显示检测到的人数
        num_label = "Human: {0}".format(len(humans))
        cv.putText(show, num_label, (5, height - 45), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        # 显示目前的运行时长及总帧数
        if frame_count == 1:
            run_timer = time.time()

        process_time = time.time() - process_start
        print(frame_count)
        print("time:")
        print(process_time)
        print("\n")
        print("----------")
        run_time = time.time() - run_timer
        time_frame_label = '[Time:{0:.2f} | Frame:{1}]'.format(run_time, frame_count)
        cv.putText(show, time_frame_label, (5, height - 15), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        # cv.imshow('Action Recognition based on OpenPose', frame) #show

        video_writer.write(frame)  # show

        # # 采集数据，用于训练过程(for training)
        # joints_norm_per_frame = np.array(pose[-1]).astype(np.str)
        # f.write(' '.join(joints_norm_per_frame))
        # f.write('\n')
    else:
        break

video_writer.release()
cap.release()
f.close()