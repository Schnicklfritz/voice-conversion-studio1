#!/usr/bin/env python3
import os
from pydub import AudioSegment
import subprocess

def fix_purple_rain():
    # 1. Resample to 40k (RVC native rate)
    subprocess.run(['sox', 'purple_rain.flac', '-r', '40000', '-b', '16', 'purple_rain_40k.wav'])
    
    # 2. Truncate at 7:15 (modulation trap fix)
    audio = AudioSegment.from_wav("purple_rain_40k.wav")
    audio[:435_000].export("truncated_40k.wav", format="wav")
    
    # 3. Apply 40k pitch fix (F# → E)
    subprocess.run(['sox', 'truncated_40k.wav', 'hendrix_ready.wav', 'speed', '0.960'])
    
    # 4. Convert with Hendrix model
    subprocess.run([
        'python', 'infer-web.py',
        '--input', 'hendrix_ready.wav',
        '--model', 'jimihendrix.pth',
        '--index', 'added_IVF1327_Flat_nprobe_1_jimihendrix_v2.index',
        '--index_rate', '0.85',
        '--f0up_key', '0',
        '--filter_radius', '6',
        '--protect', '0.25',
        '--output', 'hendrix_purple_rain.flac'
    ])

if __name__ == "__main__":
    fix_purple_rain()
