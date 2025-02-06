# Crypto News Monitor Mobile App

This is a mobile application for monitoring cryptocurrency news and tweets.

## Setup Instructions

1. Install Flutter SDK:
   - Download Flutter SDK from: https://flutter.dev/docs/get-started/install/windows
   - Extract the downloaded zip to a folder (e.g., `C:\flutter`)
   - Add Flutter to your PATH environment variable
   - Run `flutter doctor` to verify the installation

2. Install Android Studio:
   - Download from: https://developer.android.com/studio
   - Install Android SDK and Android SDK Command-line Tools
   - Create an Android Virtual Device (AVD) for testing

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
flet run main.py
```

## Building for Android

1. Make sure Flutter and Android Studio are properly set up
2. Run the build command:
```bash
flet build apk
```

The APK file will be generated in the `build/app/outputs/flutter-apk/` directory.

## Building the APK (Alternative Method)

### Option 1: Using Google Colab (Recommended)

1. Open the `build_apk.ipynb` notebook in Google Colab:
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sbcnm999/crypto-news-monitor/blob/main/mobile_app_flet_new/build_apk.ipynb)

2. Run each cell in sequence by clicking the play button or pressing Shift+Enter
3. The APK will be automatically downloaded when the build is complete
4. Install the APK on your Android device

## Features

- Real-time cryptocurrency news feed
- Tweet monitoring with sentiment analysis
- Cryptocurrency mentions tracking
- Economic indicators monitoring
- Dark mode support
- Auto-refresh functionality

## Requirements

- Python 3.11
- Flet 0.26.0
- Android 5.0 (API 21) or higher

## Installation

1. Download the latest APK from the releases page
2. Enable "Install from Unknown Sources" in your Android settings
3. Install the APK
4. Launch the app

## Development

To set up the development environment:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app locally
python main.py
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
