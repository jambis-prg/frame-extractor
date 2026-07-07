# 🎥 Frame Extractor

A high-performance Python tool for automatically extracting image frames from video datasets.

This project was designed to simplify the creation of image datasets for Computer Vision and Artificial Intelligence research by extracting frames from multiple videos while generating metadata automatically.

---

## ✨ Features

- 📁 Process all videos inside a directory
- 🎲 Random frame extraction
- 📏 Uniform frame extraction
- ⏱ Interval-based extraction
- 📄 Automatic metadata generation
- 🔢 Continuous image numbering
- 🚀 Multi-threaded processing
- 📊 Progress bars
- 📝 Logging
- ⚙ Configuration through YAML
- 🧪 Unit tests

---

# 📂 Project Structure

```text
frame-extractor/

├── config.yaml
├── README.md
├── requirements.txt
├── pyproject.toml
├── LICENSE
├── .gitignore

├── videos/
│   ├── video01.mp4
│   ├── video02.mp4
│   └── ...

├── dataset/
│   ├── images/
│   └── metadata.csv

├── logs/

├── src/
│   ├── __init__.py
│   ├── __main__.py
│   ├── constants.py
│
│   ├── core/
│   │   ├── __init__.py
│   │   ├── extractor.py
│   │   ├── downloader.py
│   │   ├── pipeline.py
│   │   ├── scanner.py
│   │   ├── numbering.py
│   │   └── metadata.py
│
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── logger.py
│   │   ├── progress.py
│   │   └── helpers.py
│
│   └── constants.py
│
├── tests/
│   ├── test_config.py
│   ├── test_extractor.py
│   ├── test_metadata.py
│   └── test_scanner.py
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/your-user/frame-extractor.git

cd frame-extractor
```

Install dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install -e .
```

---

## System Dependencies

This project requires FFmpeg for video processing.

### Ubuntu / WSL

```bash
sudo apt update
sudo apt install ffmpeg
```
---

# 🎥 Supported Video Formats

The extractor automatically searches for:

- mp4
- mkv
- avi
- mov
- webm
- mpg
- mpeg

---

# ⚙️ Configuration

Everything is configured inside `config.yaml`.

Example:

```yaml
videos_dir: videos

output_dir: dataset/images

metadata_file: dataset/metadata.csv

mode: random

frames_per_video: 300

workers: 8

image_format: jpg

random_seed: 42

overwrite: false

min_time_between_frames: 1.5
```

---

# 📸 Extraction Modes

## Random

Extracts random frames throughout the video.

```yaml
mode: random
```

---

## Uniform

Evenly distributes the extracted frames.

```yaml
mode: uniform
```

---

## Interval

Extracts one frame every N seconds.

```yaml
mode: interval

interval_seconds: 2
```

---

# ▶️ Running

Place all videos inside the `videos/` directory.

```
videos/
    video01.mp4
    video02.mp4
    video03.mp4
```

Run

```bash
python -m src.main
```

or

```bash
python src/main.py
```

---

# 📁 Output

Images are saved in

```
dataset/images/
```

Example

```
000001.jpg
000002.jpg
000003.jpg
...
```

Metadata is automatically generated

```
dataset/metadata.csv
```

Example

| image | video | frame | timestamp |
|-------|-------|-------|-----------|
|000001.jpg|video01.mp4|1582|52.41|
|000002.jpg|video01.mp4|1943|64.33|

---

# 📄 Metadata

Each extracted frame generates one row containing:

| Field | Description |
|--------|-------------|
| image | Image filename |
| video | Original video |
| frame | Frame number |
| timestamp | Time in seconds |
| width | Image width |
| height | Image height |

---

# 📝 Logs

Execution logs are saved to

```
logs/extractor.log
```

Example

```
[INFO] Found 42 videos

[INFO] Processing video01.mp4

[INFO] Extracted 300 frames

[INFO] Finished
```

---

# ⚡ Performance

The extractor processes videos concurrently.

Configure the number of workers in

```yaml
workers: 8
```

The recommended value is the number of logical CPU cores.

---

# 🛣 Roadmap

- [ ] Scene change detection
- [ ] Blur filtering
- [ ] Duplicate frame removal
- [ ] Image quality filtering
- [ ] GPU acceleration
- [ ] Video downloader integration
- [ ] Label Studio exporter
- [ ] CVAT exporter
- [ ] Automatic train/validation split
- [ ] YOLO dataset exporter

---

# 📦 Dependencies

- Python 3.11+
- OpenCV
- tqdm
- pandas
- PyYAML

---

# 🤝 Contributing

Contributions are welcome!

If you have ideas, improvements or bug fixes, feel free to open an Issue or submit a Pull Request.

---

# 📜 License

This project is licensed under the MIT License.

---

# 🎓 Citation

If this project contributes to your research, please consider citing it.

```bibtex
@software{frameextractor,
  title={Frame Extractor},
  author={João Victor Nascimento Lima},
  year={2026},
  url={https://github.com/jambis-prg/frame-extractor}
}
```

---

# ❤️ Acknowledgements

Developed for academic Computer Vision and Artificial Intelligence research.

# 👨‍💻 Author

Developed and maintained by **João Victor Nascimento Lima**.

- GitHub: https://github.com/jambis-prg
- Email: joaovictorlima20015@gmail.com
