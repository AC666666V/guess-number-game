[app]
title = 猜数字游戏
package.name = guessnumber
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv
version = 1.0

[android]
# 严格匹配工作流中安装的版本（必须一致！）
sdk = 30
build-tools = 30.0.3
min-sdk = 21
target-sdk = 30
output.dir = bin
# 调试签名（默认值，无需修改）
key.store = ~/.android/debug.keystore
key.store.password = android
key.alias = androiddebugkey
key.alias.password = android
# 支持的架构
android.arch = armeabi-v7a,arm64-v8a

[buildozer]
log_level = 2  # 详细日志，方便排查
android.accept_sdk_license = True
cache_dir = .buildozer/cache

[python]
python.version = 3.9
requirements = kivy==2.2.1,cython==0.29.36  # 与安装的版本匹配
