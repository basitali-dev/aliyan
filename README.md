
# Easy-Wav2Lip

## Overview

**Easy-Wav2Lip** is a user-friendly implementation of the Wav2Lip model designed to generate realistic lip-syncing in videos using audio input. This repository simplifies the process of using the Wav2Lip model and offers an easy-to-follow guide for setting up and running the model.

## Features

- **Simple Setup:** Get started quickly with minimal configuration required.
- **High-Quality Lip Syncing:** Generate accurate lip movements that synchronize with the provided audio.
- **Video Processing:** Process videos effortlessly, maintaining quality and detail.
- **Flexible Input:** Support for various audio and video formats.
  
## Faster:
For my 9 second 720p 60fps test clip via Colab T4:
| Original Wav2Lip | Easy-Wav2Lip |
|:-------|:-----|
| Execution time: 6m 53s | Execution time: 56s |

That's not a typo! My clip goes from almost 7 minutes to under 1 minute!

The tracking data is saved between generations of the same video, saving even more time:
| Easy-Wav2Lip on the same video again |
|:-----|
| Execution time: 25s |

## Installation

### Prerequisites

- Python 3.6 or higher
- A suitable GPU (NVIDIA preferred) for optimal performance

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/anothermartz/Easy-Wav2Lip.git
   cd Easy-Wav2Lip
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the pre-trained Wav2Lip model:
   - Download the model weights from the provided link in the original repository.

## Usage

### Lip Syncing

To generate lip-synced videos, use the following command:

```bash
python inference.py --face <path_to_video> --audio <path_to_audio> --outfile <output_filename>
```

- `<path_to_video>`: Path to the input video file.
- `<path_to_audio>`: Path to the audio file you want to sync with.
- `<output_filename>`: Desired name for the output video file.

### Example

```bash
python inference.py --face input_video.mp4 --audio input_audio.wav --outfile output_video.mp4
```

## Results

The model produces high-quality videos where lip movements are synchronized with the audio input, enhancing the overall viewing experience. For a demonstration, please refer to the examples provided in the `examples` directory.

## Troubleshooting

If you encounter any issues, please check the following:

- Ensure all dependencies are correctly installed.
- Verify the paths to your input files are correct.
- For GPU-related issues, make sure you have the appropriate drivers and CUDA toolkit installed.

## Contributing

We welcome contributions! Please fork the repository and submit a pull request with your improvements or fixes.

