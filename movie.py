from moviepy import (
    VideoClip,
    ColorClip,
    TextClip,
    CompositeVideoClip,
    vfx
)
import numpy as np
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_demo_video(output_path: str = "output.mp4") -> None:
    """
    Create a demo video using modern MoviePy 2.1.x features
    """
    clips = []
    try:
        # Create background using ColorClip
        background = ColorClip(
            size=(1280, 720),
            color=(64, 64, 164),  # Navy blue
            duration=5
        )
        clips.append(background)

        # Create text using modern TextClip
        title_text = TextClip(
            text="MoviePy Demo",
            size=(0, 0),  # Auto-size
            color='white',
            font='/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf',
            font_size=70,
            stroke_color='black',
            stroke_width=2,
            method='label',
            text_align='center',
            bg_color=None,
            transparent=True
        )

        # Apply modern effects chain
        title_text = (title_text
            .with_position('center')
            .with_duration(5)
            .with_effects([
                vfx.FadeIn(1),
                vfx.FadeOut(1)
            ]))
        clips.append(title_text)

        # Create final composition
        final = CompositeVideoClip(
            clips,
            size=(1280, 720)
        )

        # Write using modern parameters
        final.write_videofile(
            output_path,
            fps=30,
            codec='libx264',
            audio=False,
            preset='medium',
            threads=4,
            logger='bar',
            ffmpeg_params=[
                "-crf", "18",
                "-pix_fmt", "yuv420p",
                "-profile:v", "high"
            ]
        )

    except Exception as e:
        logger.error(f"Error creating video: {str(e)}")
        raise

    finally:
        # Modern cleanup
        for clip in clips:
            clip.close()

def create_advanced_video(output_path: str = "advanced_output.mp4") -> None:
    """
    Create an advanced video using modern MoviePy 2.1.x features
    """
    clips = []
    try:
        # Create background
        background = ColorClip(
            size=(1920, 1080),
            color=(20, 40, 60),
            duration=10
        )
        clips.append(background)

        # First text clip
        text1 = TextClip(
            text=f"Created by wonderfan",
            size=(0, 0),
            color='white',
            font='/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf',
            font_size=70,
            stroke_color='blue',
            stroke_width=2,
            method='label',
            text_align='center',
            bg_color=None,
            transparent=True
        )

        # Apply modern effects chain
        text1 = (text1
            .with_position('center')
            .with_duration(5)
            .with_effects([
                vfx.FadeIn(1),
                vfx.FadeOut(1),
                vfx.Rotate(lambda t: t*20)
            ]))
        clips.append(text1)

        # Second text clip
        current_time = "2025-02-14 03:42:31"
        text2 = TextClip(
            text=f"Generated at {current_time}",
            size=(0, 0),
            color='yellow',
            font='/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf',
            font_size=40,
            stroke_color='black',
            stroke_width=1,
            method='label',
            text_align='center',
            bg_color=None,
            transparent=True
        )

        # Apply modern effects
        text2 = (text2
            .with_position(('center', 400))
            .with_start(5)
            .with_duration(5)
            .with_effects([
                vfx.FadeIn(1),
                vfx.FadeOut(1)
            ]))
        clips.append(text2)

        # Create final composition
        final = CompositeVideoClip(
            clips,
            size=(1920, 1080)
        )

        # Write with modern settings
        final.write_videofile(
            output_path,
            fps=30,
            codec='libx264',
            audio=False,
            preset='medium',
            threads=4,
            logger='bar',
            ffmpeg_params=[
                "-crf", "18",
                "-pix_fmt", "yuv420p",
                "-profile:v", "high",
                "-tune", "film"
            ]
        )

    except Exception as e:
        logger.error(f"Error creating advanced video: {str(e)}")
        raise

    finally:
        # Modern cleanup
        for clip in clips:
            clip.close()

if __name__ == "__main__":
    # create_demo_video("basic_output.mp4")
    create_advanced_video("advanced_output.mp4")