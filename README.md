# Video-quality-conversion-SD-to-HD-
Develop a prototype of a video conversion process that can upscale SD resolution (640 x 480px) videos to HD resolution (1280 x 720px) using traditional interpolation techniques. The tool should efficiently resize the video frames while maintaining the overall quality. It should preserve the original audio and merge it with the upscaled video.

**Objective:**
To create a video conversion tool that:
- Upscales SD videos to HD resolution using interpolation methods.
- Preserves the original video quality to the extent possible through traditional methods like cubic interpolation.
- Ensures the audio from the original video is retained and synchronized with the upscaled video.
- Operates efficiently to process videos in a reasonable amount of time using OpenCV and FFmpeg.

**Requirements:**
The video conversion tool should:
- Use interpolation methods (e.g., cubic interpolation) to resize video frames from SD to HD resolution.
- Extract and preserve the original audio from the video, merging it back with the upscaled video.
- Be efficient and capable of handling standard video formats, ensuring that the upscaled video maintains a good quality while being processed quickly.

**Technical Specifications:**
- **Input Resolution:** 640 x 480px (SD)
- **Output Resolution:** 1280 x 720px (HD)
- **Tools Used:** OpenCV for video processing and FFmpeg for audio extraction and merging.
- **Output Format:** The output video should be saved in a commonly used format such as `.mp4` or `.avi`, with the upscaled resolution and synchronized audio.

- Directory or file structure
- input_video (place the video inside the folder named input_video)
- upscaled_video (create a folder name upscaled_video -- > output video will store here)
- video_conversion.py
