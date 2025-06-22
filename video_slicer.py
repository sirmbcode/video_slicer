from moviepy import VideoFileClip
import sys
import ast

#TODO: use list of sys args to decide
#might need a parser

def interval_slice(clip, interval):
  temp_start = 0
  end = clip.duration
  num_clips = int(end/interval)
  for i in range(1,num_clips+1):
    temp_end = temp_start+interval
    temp = clip.subclipped(temp_start,temp_end)
    temp.write_videofile(f"exports/{temp_start}-{temp_end}.mp4")
    temp_start = i * interval

def list_slice(clip):
  interval_list = sys.argv[3:]
  # get list of intervals to download
  i = 1
  for interval in interval_list:
      start,end = ast.literal_eval(interval)
      temp = clip.subclipped(start,end)
      temp.write_videofile(f"exports/{start}-{end}.mp4")

def main():
  video_file = sys.argv[1]
  clip = (VideoFileClip(video_file))
  list_or_int = sys.argv[2]
  if list_or_int == 'list':
    list_slice(clip)
  elif list_or_int == 'interval':
    #interval
    interval = int(sys.argv[3])
    interval_slice(clip, interval)

if __name__ == main():
  main()
  


# Load file "Wizards.mov" and keep only the subclip from 00:00:10 to 00:00:20
# Reduce the audio volume to 80% of its original volume





#TODO: split and write video in multiple parts listed in command line
# loop over all intervals?


# Overlay the text clip on the first video clip
# final_video = CompositeVideoClip([clip, txt_clip])