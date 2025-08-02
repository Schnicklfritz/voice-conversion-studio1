#!/bin/bash
# Mount Lightning Drive data
ln -s /data/Hendrix_PurpleRain/raw/purple_rain.flac .
ln -s /data/Hendrix_PurpleRain/models/jimihendrix.pth .
ln -s /data/Hendrix_PurpleRain/models/added_IVF*.index .

# Run conversion
python purple_rain_fixer.py

# Save output
cp hendrix_purple_rain.flac /data/Hendrix_PurpleRain/processed/
