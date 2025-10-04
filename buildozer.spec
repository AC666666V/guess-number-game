[app]
# 应用基础信息（必填，直接影响APK标识和显示）
title = 猜数字游戏                  # 应用名称（将显示在手机桌面）
package.name = guessnumbergame      # 包名（全小写，建议用项目名，如"mygame"）
package.domain = org.example        # 域名（格式：org/公司/个人标识，如"com.myname"）
source.dir = .                      # 源代码根目录（默认当前目录，无需修改）
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf  # 打包时包含的文件类型（按需添加）
version = 1.0                       # 应用版本号（首次构建建议1.0）

# 资源文件配置（可选，无则注释或删除）
icon.filename = %(source.dir)s/icon.png      # 应用图标路径（建议512x512px）
presplash.filename = %(source.dir)s/splash.png  # 启动页图片路径（建议1080x1920px）
presplash.landscape.filename = %(source.dir)s/splash_land.png  # 横屏启动页（可选）

# 权限配置（Android需要的系统权限，按需添加）
android.permissions = INTERNET,ACCESS_NETWORK_STATE  # 示例：网络权限（不需要可删除）


[android]
# 核心构建配置（必填，版本必须匹配，否则构建失败）
sdk = 30                     # Android SDK版本（推荐30，兼容Android 5.0+）
build-tools = 30.0.3         # 对应SDK的构建工具版本（必须与sdk匹配）
min-sdk = 21                 # 最低支持Android版本（21=Android 5.0，覆盖多数设备）
target-sdk = 30              # 目标Android版本（与sdk一致）

# 签名配置（调试阶段用默认值，发布时需替换为自己的签名）
key.store = ~/.android/debug.keystore  # 调试签名文件路径（系统默认）
key.store.password = android          # 签名密码（默认调试密码）
key.alias = androiddebugkey           # 密钥别名（默认调试别名）
key.alias.password = android          # 别名密码（默认调试密码）

# 输出与架构配置
output.dir = bin              # APK生成目录（与工作流上传路径对应，默认即可）
android.arch = armeabi-v7a,arm64-v8a  # 支持的CPU架构（32位+64位，覆盖多数设备）

# 额外构建参数（可选）
android.add_src = False       # 是否添加额外源码目录（默认关闭）
android.enable_androidx = True  # 启用AndroidX（现代Android项目必需）
android.gradle_dependencies =  # 额外Gradle依赖（如第三方库，无则留空）


[ios]
# iOS构建配置（如果不需要iOS，可忽略或保持默认）
ios.sdk = 15.5               # iOS SDK版本（仅iOS构建需要）
ios.codesign.identity = iPhone Developer  # 签名身份（开发证书）
# 其他iOS参数（非必要，不构建iOS可不动）


[buildozer]
# Buildozer工具配置（影响构建过程）
log_level = 2                # 日志级别（0=静默，2=详细，建议调试用2）
warn_on_root = 1             # 根目录构建时警告（1=开启，避免权限问题）
android.accept_sdk_license = True  # 自动接受SDK许可（关键：替代手动操作）
build_dir = .buildozer       # 构建临时文件目录（默认即可，自动创建）
cache_dir = .buildozer/cache # 缓存目录（加速重复构建，建议保留）


[python]
# Python环境配置（需与工作流中Python版本一致）
python.version = 3.9         # Python版本（与工作流中setup-python的版本匹配）
requirements = kivy==2.2.1,cython==0.29.36  # 项目依赖库（必填，按实际需求添加）
# 示例：如果用了requests库，添加",requests==2.31.0"
pyzbar = False               # 是否包含pyzbar库（默认关闭，需要则设为True）


[armeabi-v7a]
# 32位ARM架构配置（默认即可）
android.arch = armeabi-v7a   # 架构标识（无需修改）


[arm64-v8a]
# 64位ARM架构配置（默认即可）
android.arch = arm64-v8a     # 架构标识（无需修改）


[x86]
# x86架构配置（可选，适配模拟器，默认关闭）
android.arch = x86           # 如需支持x86设备，取消注释


[x86_64]
# x86_64架构配置（可选）
android.arch = x86_64        # 如需支持x86_64设备，取消注释
