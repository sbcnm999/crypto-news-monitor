[app]
title = Crypto News Monitor
package.name = crypto_news_monitor
package.domain = com.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0.0
requirements = python3,flet==0.26.0,requests,python-dateutil,pillow
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.permissions = INTERNET
android.arch = arm64-v8a
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license = True
android.gradle_dependencies = org.jetbrains.kotlin:kotlin-stdlib-jdk7:1.7.10
p4a.branch = master
p4a.bootstrap = webview

[buildozer]
log_level = 2
warn_on_root = 1
