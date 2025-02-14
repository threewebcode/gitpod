import os
from moviepy.editor import ColorClip, TextClip, CompositeVideoClip, concatenate_videoclips
from moviepy.audio.io.AudioFileClip import AudioFileClip
from elevenlabs import ElevenLabs

# Set your API key
API_KEY = os.getenv('ELEVENLABS_API_KEY')
if not API_KEY:
    raise ValueError("ElevenLabs API key not found. Set ELEVENLABS_API_KEY in your environment.")

client = ElevenLabs(api_key=API_KEY)

def read_text_file(file_path="text.txt"):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        sections = content.split('\n\n')
        return [section.strip() for section in sections if section.strip()]
    except IOError:
        print(f"Error: Could not read file {file_path}")
        return []

def generate_audio(text, output_file="generated_audio.mp3"):
    if os.path.exists(output_file):
        print(f"Audio file {output_file} already exists. Skipping API call.")
        return output_file

    try:
        # You can customize these parameters based on your needs
        audio = client.text_to_speech.convert(
            voice_id="JBFqnCBsd6RMkjVDRZzb",  # Example voice ID, replace with your preferred voice
            output_format="mp3_44100_128",  # MP3 format at 44.1kHz with 128kbps bitrate
            text=text,
            model_id="eleven_multilingual_v2"  # Example model ID, check ElevenLabs docs for options
        )
        
        # Convert generator to bytes
        audio_bytes = b''.join(audio)
        
        with open(output_file, 'wb') as f:
            f.write(audio_bytes)
        print(f"Audio file generated: {output_file}")
        return output_file
    except Exception as e:
        print(f"Error generating audio via ElevenLabs API: {e}")
        return None

def generate_video_clips(sections):
    clips = []
    for i, section in enumerate(sections, 1):
        try:
            # Create a solid color background
            background = ColorClip((640, 480), color=(255, 255, 255)).set_duration(2)  # White background, 2 seconds duration

            # Add text over the background
            text_clip = TextClip(section, fontsize=24, color='black', font='Arial-Bold', size=(640, 480))
            text_clip = text_clip.set_position(('center', 'center'))

            # Combine background with text
            composite_clip = CompositeVideoClip([background, text_clip], size=(640, 480))
            clips.append(composite_clip)
            print(f"Generated clip {i} of {len(sections)}")
        except Exception as e:
            print(f"Error generating clip for section {section}: {e}")
    return clips

def create_video(clips, audio_file, output_video="output_video.mp4"):
    try:
        if not audio_file:
            raise ValueError("No audio file provided")

        # Concatenate all text clips
        video_clip = concatenate_videoclips(clips)

        # Load the generated audio
        audio = AudioFileClip(audio_file)

        # Adjust audio and video duration for synchronization
        if audio.duration > video_clip.duration:
            audio = audio.subclip(0, video_clip.duration)  # Trim audio to match video duration
        elif audio.duration < video_clip.duration:
            video_clip = video_clip.loop(duration=audio.duration)  # Loop video to match audio duration

        # Composite the audio with the video
        final_clip = video_clip.set_audio(audio)

        # Write the video file
        final_clip.write_videofile(output_video, fps=24, codec="libx264", audio_codec="aac")
        print(f"Video created: {output_video}")
        return output_video
    except Exception as e:
        print(f"Error creating video: {e}")
        return None

# Main execution
def main():
    sections = read_text_file("text.txt")
    if not sections:
        return

    # Combine all sections for audio generation
    full_text = " ".join(sections)
    audio_file = generate_audio(full_text)

    if audio_file:
        video_clips = generate_video_clips(sections)
        if video_clips:
            create_video(video_clips, audio_file)
        else:
            print("No video clips were generated to combine.")
        
        # Clean up temporary audio file
        os.remove(audio_file)
    else:
        print("No audio file was generated.")

if __name__ == "__main__":
    main()