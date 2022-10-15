import wget
import ffmpeg
import moviepy.editor as mp

# Stage I: Downloading the Video
url_link= 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4'
filename = wget.download(url_link)
filename = filename[:-4]

# Stage II: Scaling Down the video
clip = mp.VideoFileClip(filename+".mp4")
clip_resized = clip.resize(height=360) #(width/height ratio is conserved)
filename2 = filename + "_resized"
clip_resized.write_videofile(filename2+".mp4")

# Stage III: Cropping the Video
filename3 = filename +"_cropped"
stream = ffmpeg.input(filename2+".mp4")
stream = ffmpeg.crop(stream, 50, 50, 256, 256)

# Stage IV: Saving
stream = ffmpeg.output(stream, filename3+".mp4")
ffmpeg.run(stream)