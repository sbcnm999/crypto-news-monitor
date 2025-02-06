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

## Features

- Real-time cryptocurrency news feed
- Tweet monitoring with sentiment analysis
- Cryptocurrency mentions tracking
- Economic indicators monitoring
- Dark mode support
- Auto-refresh functionality
