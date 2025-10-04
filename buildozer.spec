[app]

# 应用名称（手机桌面显示）
title = 猜数字游戏

# 包名（唯一标识）
package.name = guessnumbergame

# 域名
package.domain = org.guessgame

# 代码目录
source.dir = .

# 包含文件类型
source.include_exts = py,kv,png,jpg

# 应用版本
version = 1.0

# 依赖库（确保手机兼容性）
requirements = python3,kivy==2.3.1,pyjnius==1.5.0  # 增强安卓交互支持

# 强制竖屏（手机主要使用场景）
orientation = portrait

# 支持沉浸式状态栏（更美观）
android:theme = @android:style/Theme.NoTitleBar.Fullscreen


[buildozer]

log_level = 2
warn_on_root = 1


[android]

# 适配更多安卓设备架构
android.arch = armeabi-v7a,arm64-v8a  # 新增64位架构支持

# 最低支持安卓5.0（覆盖95%设备）
android.minapi = 21

# 目标安卓版本（最新稳定版）
android.targetapi = 34

# 允许安装后在桌面显示图标
android.icon = icon.png  # 可选，放一张icon.png到项目根目录

# 测试版无需签名
android.sign = False

# 允许横屏切换（虽然默认竖屏，但留有余地）
android.allow_landscape = False