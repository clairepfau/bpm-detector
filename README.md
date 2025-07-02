# BPM Detector

A Python tool that automatically detects the tempo (BPM) of audio files using onset detection and autocorrelation analysis.

## How It Works

The detector analyzes audio files by:
1. **Onset Detection** - Identifies points where the audio signal changes significantly
2. **Autocorrelation** - Finds repeating patterns in these onset points
3. **Peak Detection** - Locates the strongest rhythmic patterns
4. **BPM Calculation** - Converts the average time between beats to beats per minute

## Features

- Supports common audio formats (WAV, MP3, FLAC, etc.)
- Uses librosa's robust audio analysis algorithms
- Command-line interface for easy integration
- Error handling for invalid files

## Installation

```bash
pip install librosa numpy
```

## Usage

### Command Line
```bash
python bpm_detector.py path/to/your/audio/file.wav
```

### As a Module
```python
from bmp_detector import detect_bpm

bpm = detect_bpm('song.wav')
print(f"Detected BPM: {bpm:.1f}")
```

## Example Output

```
Sample Rate: 22050 Hz
Audio length: 3751936 samples → 170.15 seconds
Detected BPM: 170.2
```

## Technical Details

- Uses librosa's onset strength detection with default parameters
- Applies autocorrelation to find periodic patterns
- Peak picking parameters tuned for typical music BPM ranges (60-200 BPM)
- Frame-based analysis with 512-sample hop length

## Limitations

- Works best with music that has a consistent beat
- May struggle with very complex polyrhythms or tempo changes
- Requires clear percussive elements for accurate detection

## Requirements

- Python 3.6+
- librosa
- numpy

# Project reformatted for proffessional presentation with Claude AI