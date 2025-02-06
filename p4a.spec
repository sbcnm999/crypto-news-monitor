[app]
name = CryptoNewsMonitor
package.name = com.example.crypto_news_monitor
version = 1.0.0
bootstrap = webview

requirements = python3,flet==0.26.0,requests,python-dateutil,pillow

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.private_storage = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
