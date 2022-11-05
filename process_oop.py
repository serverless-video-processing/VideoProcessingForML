import wget
import moviepy.editor as mp
from memory_profiler import profile
import moviepy.video.fx.all.crop as mp_crop

@profile
def download(url_link):
    filename = wget.download(url_link)
    filename = filename[:-4]
    return filename

@profile
def scaleDown(filename):
    clip = mp.VideoFileClip(filename+".mp4")
    clip_resized = clip.resize(height=360) #(width/height ratio is conserved)
    outputFilename = filename + "_resized"
    clip_resized.write_videofile(outputFilename+".mp4")
    return outputFilename

@profile
def crop(filename):
    outputFilename = filename +"_cropped"
    stream = mp.VideoFileClip(filename+".mp4")
    stream = mp_crop(stream, 256, 256, 256//2, 256//2)
    # Stage IV: Saving
    stream.write_videofile(outputFilename+".mp4")

@profile
def pipeline():
    # Stage I: Downloading the Video
    url_link= 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4'
    filename = download(url_link)

    # Stage II: Scaling Down the video
    scaledDownFilename = scaleDown(filename)

    # Stage III+IV: Cropping the Video and saving it using ffmpeg
    crop(scaledDownFilename)

if __name__=="__main__":
    pipeline()