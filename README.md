# Sit Window

A phone web app that scores every morning, midday, and evening deer-hunting sit for the next 7 days at a backyard bow blind in West Milford, NJ, and picks the best 3.

- **Weather:** live hourly forecast from [Open-Meteo](https://open-meteo.com/) (free, no key), fetched by the phone.
- **Scoring:** a transparent point system. Tap any sit to see the math. Factors are time of day, rut timing, wind direction for the blind (south is best, north is a bad sit), wind speed, temperature drop, pressure trend, rain, and your own daylight sightings. Moon phase is shown and worth 0 points.
- **Sightings:** log deer seen from the blind or on the trail camera. They're stored on the phone, with an export and import backup.

## Files
- `src/sit-window.html`: the app source, also published as a Claude artifact.
- `build.py`: wraps the source into `index.html` for GitHub Pages. Run `python3 build.py` after editing the source.
- `manifest.webmanifest`, `icon*.png`, `icon.svg`: home-screen install.

## Add to your home screen
Open the GitHub Pages link in Safari, tap Share, then tap **Add to Home Screen**.
