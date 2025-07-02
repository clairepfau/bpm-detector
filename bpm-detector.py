import librosa
import numpy as np
import argparse
import os

def detect_bpm(audio_path):
    """
    Detect BPM of an audio file using onset detection and autocorrelation.
    
    Args:
        audio_path (str): Path to the audio file
        
    Returns:
        float: Detected BPM
    """
    # Load audio file
    y, sr = librosa.load(audio_path)
    
    print(f"Sample Rate: {sr} Hz")
    print(f"Audio length: {len(y)} samples → {len(y)/sr:.2f} seconds")
    
    # Calculate onset strength - measures how much the audio changes at each time frame
    onset_strength = librosa.onset.onset_strength(y=y, sr=sr)
    
    # Use autocorrelation to find repeating patterns in onset strength
    autocorr = librosa.autocorrelate(onset_strength)
    
    # Find peaks in the autocorrelation that represent potential beat intervals
    bpm_candidates = librosa.util.peak_pick(
        autocorr,
        pre_max=3,      # Frames before peak that must be lower
        post_max=3,     # Frames after peak that must be lower  
        pre_avg=3,      # Frames to average before peak
        post_avg=5,     # Frames to average after peak
        delta=0.5,      # Minimum height difference
        wait=10         # Minimum frames between peaks
    )
    
    if len(bpm_candidates) < 2:
        return None
    
    # Convert frame indices to time (default hop length is 512 samples)
    hop_length = 512
    candidate_times = bpm_candidates * (hop_length / sr)
    
    # Calculate intervals between beat candidates
    intervals = np.diff(candidate_times)
    
    # Average interval gives us the beat period
    avg_interval = np.mean(intervals)
    
    # Convert to BPM (60 seconds / average interval between beats)
    bpm = 60 / avg_interval
    
    return bpm

def main():
    parser = argparse.ArgumentParser(description='Detect BPM of an audio file')
    parser.add_argument('audio_file', help='Path to audio file')
    args = parser.parse_args()
    
    if not os.path.exists(args.audio_file):
        print(f"Error: File '{args.audio_file}' not found")
        return
    
    try:
        bpm = detect_bpm(args.audio_file)
        if bpm:
            print(f"\nDetected BPM: {bpm:.1f}")
        else:
            print("Could not detect BPM - not enough beat candidates found")
    except Exception as e:
        print(f"Error processing audio file: {e}")

if __name__ == "__main__":
    # Example usage with hardcoded file (remove this in final version)
    test_file = '/home/claire/Code/bpm-analyzer/test_audio/test_sound_for_bpm_option1_170bpm.wav'
    if os.path.exists(test_file):
        print("Testing with sample file:")
        bpm = detect_bpm(test_file)
        if bpm:
            print(f"Detected BPM: {bpm:.1f}")
    
    # Uncomment this line to enable command line usage:
    # main()