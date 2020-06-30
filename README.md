# video2bag
package for processing video file(.mp4) to **rosbag(.bag)** file

## prerequisites
- opencv-python
- cv_bridge
- rosbag
- glob
- regex

## Installation 
**pip** : glob, regex <br>
**apt** : opencv-python, ros-{distro}-cv-bridge, ros-{distro}-desktop-full

## Instructions
### 1. Extract frame by using extract_frame.py
```
python extract.py
```

indicate the directories of your input video and output frame in the extract_frame.py file 

### 2. Run video2bag.py to make rosbag file

```
python video2bag.py
```
