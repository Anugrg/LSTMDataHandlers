import os
from pathlib import Path
import numpy as np



'''
f = Path.cwd()

ff = Path(f / "processed")

print(ff)
'''
'''
ndim, dt = 4, 1.
# Create Kalman filter model matrices.

_motion_mat = np.eye(2 * ndim, 2 * ndim)
print(_motion_mat)


for i in range(ndim):
     _motion_mat[i, ndim + i] = dt
_update_mat = np.eye(ndim, 2 * ndim)
print("after insertion:")
print(_motion_mat)

print("------------")
print(_update_mat)
'''
args = "video.mp4"
file_path = Path.cwd()
out_file_path = Path(file_path / "test_out/")
out_file_path = str(out_file_path / (str(args).strip(".mp4")+'_tf_out.mp4'))
print(out_file_path)
realtime_fps = 1
fps_label = 'FPS:{0:.2f}'.format(realtime_fps)

print (fps_label)
