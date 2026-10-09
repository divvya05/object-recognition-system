---
title: Object Identifier ML
emoji: 🏢
colorFrom: pink
colorTo: blue
sdk: gradio
sdk_version: 6.30.0
python_version: '3.12'
app_file: app.py
pinned: false
---

## JupyterLab-first Object Recognition

The deployed app is available at
[Summer101xoxo/Object_Identifier_ML](https://huggingface.co/spaces/Summer101xoxo/Object_Identifier_ML).

The primary project workflow is in JupyterLab:

- `object_recognition_app.ipynb` runs the image/video detection interface and
  forwards uploads to the public
[Object Recognition Space](https://huggingface.co/spaces/shaheerawan3/Object_Recognition_Space).
- `cifar10_exploration.ipynb` loads and explores the CIFAR-10 dataset.

`app.py` is retained as the Gradio entry point required by Hugging Face Spaces.
The Space uses ZeroGPU-decorated callbacks as required by its selected
hardware; object detection itself is handled by the linked detector Space.
Run the notebooks for the project workflow. For a private remote detector, set
`HF_TOKEN` in the environment before launching the app notebook.

Use Python 3.12 for the local notebook kernel; this matches the Space runtime
and supports the TensorFlow dependency. On Windows, create the project
environment and start JupyterLab with:

```powershell
python -m pip install --user uv
python -m uv python install 3.12
python -m uv venv --python 3.12 .venv
python -m uv pip install --python .venv\Scripts\python.exe -r requirements.txt
.\.venv\Scripts\python.exe -m ipykernel install --user --name object-recognition --display-name "Python 3.12 (Object Recognition)"
.\.venv\Scripts\jupyter.exe lab
```

Open `object_recognition_app.ipynb` and select the **Python 3.12 (Object
Recognition)** kernel, then run its cells from top to bottom. Its last cell
launches the Gradio interface inside the notebook.

Run `cifar10_exploration.ipynb` separately to explore CIFAR-10; its first run
downloads the dataset. Hugging Face Spaces uses `app.py` as its required
deployment entry point.
