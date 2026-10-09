import os
from functools import lru_cache

import gradio as gr
from gradio_client import Client, handle_file


SPACE_ID = "shaheerawan3/Object_Recognition_Space"


@lru_cache(maxsize=1)
def get_space_client():
    """Create one client for the remote object-recognition Space."""
    return Client(SPACE_ID, hf_token=os.environ.get("HF_TOKEN"))


def process_static_image(image_path):
    """Forward an uploaded image to the Space's static-image endpoint."""
    if image_path is None:
        return None, "Please upload an image"

    return get_space_client().predict(
        image=handle_file(image_path),
        api_name="/process_static_image",
    )


def process_video(video_path):
    """Forward an uploaded video to the Space's video-processing endpoint."""
    if video_path is None:
        return None, "Please upload a video"

    video_file = video_path.get("video") if isinstance(video_path, dict) else video_path
    if video_file is None:
        return None, "Please upload a video"

    return get_space_client().predict(
        video_path={"video": handle_file(video_file)},
        api_name="/process_video",
    )


with gr.Blocks(title="AI Object Recognition System", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🤖 AI Object Recognition System
    ### Intelligent Auto-Adjusting Detection & Tracking

    This interface sends uploaded media to the
    [Object Recognition Space](https://huggingface.co/spaces/shaheerawan3/Object_Recognition_Space),
    which automatically optimizes detection based on media characteristics and
    available resources.

    **No manual tuning required!**
    """)

    with gr.Tabs():
        with gr.Tab("📸 Static Mode - Image Detection"):
            gr.Markdown("""
            ### Automatic Image Analysis
            Upload an image to automatically adjust detection settings, find
            visible objects, and provide detailed statistics.
            """)

            with gr.Row():
                with gr.Column():
                    static_input = gr.Image(type="filepath", label="Upload Image")
                    static_btn = gr.Button(
                        "🔍 Auto-Detect Objects", variant="primary", size="lg"
                    )
                    gr.Markdown("*Detection is processed by the connected Hugging Face Space.*")

                with gr.Column():
                    static_output = gr.Image(label="Detected Objects")
                    static_summary = gr.Markdown(label="Detection Results")

            static_btn.click(
                fn=process_static_image,
                inputs=[static_input],
                outputs=[static_output, static_summary],
            )

            gr.Examples(
                examples=[],
                inputs=static_input,
                label="Try these examples (upload your own images)",
            )

        with gr.Tab("🎥 Dynamic Mode - Video Detection"):
            gr.Markdown("""
            ### Automatic Video Analysis
            The connected Space automatically selects frame sampling and
            confidence settings based on the uploaded video and available resources.
            """)

            with gr.Row():
                with gr.Column():
                    video_input = gr.Video(label="Upload Video")
                    video_btn = gr.Button(
                        "🎬 Auto-Process Video", variant="primary", size="lg"
                    )
                    gr.Markdown("*Video processing is performed by the connected Hugging Face Space.*")

                with gr.Column():
                    video_output = gr.Video(label="Processed Video with Detections")
                    video_summary = gr.Markdown(label="Processing Results")

            video_btn.click(
                fn=process_video,
                inputs=[video_input],
                outputs=[video_output, video_summary],
            )

    gr.Markdown("""
    ---
    ### 💡 Tips
    - Clear, well-lit images and videos generally produce the best results.
    - Processing time depends on media length and the remote Space's availability.
    - Configure `HF_TOKEN` in the environment if connecting to a private Space.
    """)


if __name__ == "__main__":
    demo.launch()
