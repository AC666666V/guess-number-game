[app]
# 应用名称（自定义）
title = 猜数字游戏
# 应用包名（格式：域名.公司.应用，全小写）
package.name = guessnumber
# 域名（自定义，确保全小写）
package.domain = org.example

[android]
# 使用稳定的Android SDK版本（30兼容性最佳）
sdk = 30
# 对应SDK的构建工具版本（必须与SDK版本匹配）
build-tools = 30.0.3
# 最小支持的Android版本（可选，如21支持Android 5.0+）
min-sdk = 21
# 目标Android版本（与SDK版本一致）
target-sdk = 30
# 签名配置（调试版可省略，发布版需配置）
# key.store = ~/.android/debug.keystore
# key.store.password = android
# key.alias = androiddebugkey
# key.alias.password = android
