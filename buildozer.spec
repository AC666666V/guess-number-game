[app]
title = 猜数字游戏
package.name = guessnumber
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv
version = 1.0

# 可选：应用图标（如需添加，将图片放在根目录并取消注释）
# icon.filename = %(source.dir)s/icon.png

android.permissions = 

[android]
sdk = 30
build-tools = 30.0.3
min-sdk = 21
target-sdk = 30
output.dir = bin
key.store = ~/.android/debug.keystore
key.store.password = android
key.alias = androiddebugkey
key.alias.password = android
android.arch = armeabi-v7a,arm64-v8a

[buildozer]
log_level = 2
android.accept_sdk_license = True
cache_dir = .buildozer/cache

[python]
python.version = 3.9
requirements = kivy==2.2.1,cython==0.29.36
