[app]
title = Crypto News Monitor
package.name = crypto_news_monitor
package.domain = com.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0.0
requirements = python3,kivy,flet==0.26.0,requests,python-dateutil,pillow,kivymd
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.2.1
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license = True
android.gradle_dependencies = org.jetbrains.kotlin:kotlin-stdlib-jdk7:1.7.10
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE
android.presplash_color = #FFFFFF
p4a.branch = master
p4a.bootstrap = webview

[buildozer]
log_level = 2
warn_on_root = 1
