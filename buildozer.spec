[app]

# APP名称（手机上显示的名字）
title = 猜数字游戏

# 包名（小写，无空格，唯一标识）
package.name = guessnumbergame

# 域名（测试用，随便填）
package.domain = org.guessgame

# 代码目录（当前文件夹）
source.dir = .

# 包含的文件类型（代码和资源）
source.include_exts = py,kv,png,jpg,ttf

# 应用版本
version = 1.0

# 依赖库（必须包含kivy）
requirements = python3,kivy

# 支持的屏幕方向（竖屏为主）
orientation = portrait

# 使用清华源加速下载
pypi_index_url = https://pypi.tuna.tsinghua.edu.cn/simple


[buildozer]

# 日志级别（2=调试模式，打包出错时方便排查）
log_level = 2

# 根用户警告（默认即可）
warn_on_root = 1


[android]

# 是否全屏（0=非全屏）
fullscreen = 0

# 安卓架构（兼容多数设备）
android.archs = arm64-v8a,armeabi-v7a

# 最低支持安卓版本（5.0及以上）
android.minapi = 21

# 目标安卓版本
android.targetapi = 33

# 测试版无需签名
android.sign = False

# 添加权限（如果需要网络等）
# android.permissions = INTERNET

# 指定字体文件夹
android.add_src = ./fonts/*.ttf