@echo off
echo Building APK with Docker...

rem Build Docker image
docker build -t android-builder .

rem Run container to build APK
docker run --rm -v "%CD%:/app" android-builder

echo Build complete! Check app/build/outputs/apk/release/ for the APK file.
