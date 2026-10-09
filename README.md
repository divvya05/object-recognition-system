---
title: Object Recognition Space
emoji: 🐠
colorFrom: pink
colorTo: red
sdk: gradio
sdk_version: 5.49.1
app_file: app.py
pinned: false
license: apache-2.0
---

The primary project workflow is in JupyterLab:

- `object_recognition_app.ipynb` runs the image/video detection interface and
  forwards uploads to the public
[Object Recognition Space](https://huggingface.co/spaces/shaheerawan3/Object_Recognition_Space).
- `cifar10_exploration.ipynb` loads and explores the CIFAR-10 dataset.

`app.py` provides the equivalent object-recognition interface as the entry
point required to deploy this project as a Hugging Face Space. For a private
remote Space, set `HF_TOKEN` in the environment before running either app.

## Run the app

Install dependencies and start JupyterLab from the project folder:

```bash
pip install -r requirements.txt
jupyter lab
```

Open `object_recognition_app.ipynb` in JupyterLab and run its cells from top to
bottom. The final cell launches the Gradio interface inside the notebook.

To launch the deployment entry point outside the notebook, run:

```bash
python app.py
```

Run `cifar10_exploration.ipynb` separately to explore CIFAR-10; its first run
downloads the dataset.

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
