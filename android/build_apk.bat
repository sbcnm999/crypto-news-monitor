@echo off
setlocal

rem Set Android SDK path
set "ANDROID_HOME=%LOCALAPPDATA%\Android\Sdk"
set "PATH=%PATH%;%ANDROID_HOME%\tools;%ANDROID_HOME%\platform-tools"

rem Find Android Studio and its bundled JDK
for /d %%i in ("%LOCALAPPDATA%\Android\*") do (
    if exist "%%i\jbr" set "JAVA_HOME=%%i\jbr"
)

if not defined JAVA_HOME (
    for /d %%i in ("%PROGRAMFILES%\Android\Android Studio\jbr") do (
        if exist "%%i" set "JAVA_HOME=%%i"
    )
)

if not defined JAVA_HOME (
    for /d %%i in ("%PROGRAMFILES%\Java\jdk*") do (
        if exist "%%i" set "JAVA_HOME=%%i"
    )
)

if not defined JAVA_HOME (
    echo Java not found. Please install Java or Android Studio.
    exit /b 1
)

echo Using JAVA_HOME: %JAVA_HOME%
set "PATH=%JAVA_HOME%\bin;%PATH%"

rem Run Gradle build
call gradlew.bat assembleRelease

if %ERRORLEVEL% EQU 0 (
    echo Build successful! APK location: app\build\outputs\apk\release\app-release.apk
) else (
    echo Build failed with error code %ERRORLEVEL%
)

endlocal
