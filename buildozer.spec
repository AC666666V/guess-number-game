[app]
title = 猜数字游戏
package.name = guessnumberpro
package.domain = org.guessgamepro
source.dir = .
# 包含根目录的字体文件（如果存在）
source.include_exts = py,kv,ttf,png,jpg
version = 1.2
# 依赖库：确保安卓端字体渲染正常
requirements = python3,kivy==2.3.1,pyjnius==1.5.0
orientation = portrait
# 安卓主题：避免状态栏遮挡文字
android:theme = @android:style/Theme.NoTitleBar.Fullscreen

[buildozer]
log_level = 2
warn_on_root = 1

[android]
# 适配32/64位安卓设备
android.archs = armeabi-v7a,arm64-v8a
android.minapi = 21
android.targetapi = 34
# 移除了对缺失字体文件的引用
# 测试版无需签名
android.sign = False
# 保存最佳成绩（可选）
android.allow_backup = True