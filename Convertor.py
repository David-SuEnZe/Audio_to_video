from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip

# 路径设置
audio_path = "/Users/david/Desktop/Master/Period 5/Additive Manufacturing in Industry - Project Course/Recordings/Meeting1.m4a"  # 音频文件路径
image_path = "/Users/david/Desktop/Master/Period 5/Additive Manufacturing in Industry - Project Course/Recordings/030CA034129912F3C924867BA7ECC3C9.jpg"  # 图片文件路径
output_video_path = "/Users/david/Desktop/Master/Period 5/Additive Manufacturing in Industry - Project Course/Recordings/meeting1.mp4"  # 输出视频文件路径

# 加载图片和音频到 moviepyp
image_clip = ImageClip(image_path)
audio_clip = AudioFileClip(audio_path)

# 设置图片剪辑的持续时间与音频相同
image_clip = image_clip.set_duration(audio_clip.duration)

# 创建视频剪辑
video = CompositeVideoClip([image_clip.set_audio(audio_clip)])
print("About to write video file.")
# 保存视频
video.write_videofile(output_video_path, codec="libx264", fps=24)