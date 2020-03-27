import cv2
import collections
import numpy as np

def video_to_img(video_path,save_path,is_merged=False,merge_size=10):
    """
    Extract frame from video as image
    :param video_path: path to video file
    :param save_path: output path
    :param is_merged: combine multiple past frames as single frame or not.
    :param merge_size: No. of past frames to be merged as one single frame
    :return:
    """
    #video_path='1.webm'
    fname=video_path
    if video_path.rfind('/')!=-1:
        fname=video_path[video_path.rfind('/')+1:]
    frame_buffer=collections.deque(maxlen=merge_size)
    video=cv2.VideoCapture(video_path)
    frame_count=0
    while True:
        isok,frame=video.read()
        if not isok:
            break
        frame = cv2.resize(frame, (320,240), interpolation = cv2.INTER_AREA)
        if is_merged:
            if len(frame_buffer)==0:
                for i in range(merge_size):
                    frame_buffer.append(frame)
            frame_buffer.append(frame)
            frame_out=np.sum(list(frame_buffer),0)
            frame_out=frame_out/merge_size
            frame_out.astype(int)
        else:
            frame_out=frame
        cv2.imwrite(save_path+fname+str(frame_count).zfill(5)+'.jpg',frame_out)
        # cv2.imshow('a',frame)
        # cv2.waitKey(100)
        frame_count+=1

video_to_img('1.webm','',True,merge_size=3)