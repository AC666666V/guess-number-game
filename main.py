from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import platform
from kivy.core.text import LabelBase
import random
import os

# 注册中文字体
font_path = os.path.join(os.path.dirname(__file__), 'fonts', 'DroidSansFallback.ttf')
chinese_font_registered = False
if os.path.exists(font_path):
    LabelBase.register(name='Chinese', fn_regular=font_path)
    chinese_font_registered = True

# 设置窗口大小以模拟移动设备（仅在桌面环境）
if platform not in ('android', 'ios'):
    Window.size = (360, 640)
    Window.title = '猜数字游戏'


class GameLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 初始化1-100的随机数
        self.target_number = random.randint(1, 100)
        # 记录猜测次数
        self.guess_count = 0
        # 记录游戏历史
        self.history = []

    def check_guess(self):
        # 获取用户输入
        input_text = self.ids.number_input.text.strip()

        # 验证输入是否为空
        if not input_text:
            self.show_popup("提示", "请输入数字再猜哦~")
            return

        # 验证输入是否为数字
        try:
            user_guess = int(input_text)
        except ValueError:
            self.show_popup("错误", "请输入有效的数字！")
            self.ids.number_input.text = ""  # 清空无效输入
            return

        # 验证数字范围
        if user_guess < 1 or user_guess > 100:
            self.show_popup("提示", "请输入1-100之间的数字！")
            self.ids.number_input.text = ""
            return

        # 猜测次数+1
        self.guess_count += 1

        # 判断大小
        if user_guess < self.target_number:
            hint = f"{user_guess} 太小啦！再试一次"
            self.ids.hint_label.text = hint
            self.history.append(f"{user_guess} (太小)")
        elif user_guess > self.target_number:
            hint = f"{user_guess} 太大啦！再试一次"
            self.ids.hint_label.text = hint
            self.history.append(f"{user_guess} (太大)")
        else:
            hint = f"恭喜猜对啦！就是 {user_guess} ！\n共猜了{self.guess_count}次"
            self.ids.hint_label.text = hint
            self.history.append(f"{user_guess} (正确!)")
            self.show_popup("恭喜", f"猜对啦！答案是 {user_guess}\n共猜了 {self.guess_count} 次")
            # 猜对后重置游戏
            self.reset_game()

        # 更新历史记录显示
        self.update_history()
        # 清空输入框
        self.ids.number_input.text = ""

    def reset_game(self):
        """重置游戏"""
        self.target_number = random.randint(1, 100)
        self.guess_count = 0
        self.history = []
        self.ids.hint_label.text = "我想了一个1-100的数字，猜猜看？"
        self.update_history()

    def update_history(self):
        """更新历史记录显示"""
        if self.history:
            self.ids.history_label.text = "猜测历史:\n" + "\n".join(self.history[-5:])  # 只显示最近5条
        else:
            self.ids.history_label.text = "暂无猜测记录"

    def show_popup(self, title, content):
        """显示弹窗"""
        # 根据是否有中文字体决定使用哪种字体
        if chinese_font_registered:
            popup_content = Label(text=content, font_size=18, font_name='Chinese')
        else:
            popup_content = Label(text=content, font_size=18)
            
        popup = Popup(
            title=title,
            content=popup_content,
            size_hint=(0.8, 0.4)
        )
        popup.open()


class GuessNumberApp(App):
    # 手动指定kv文件（避免自动命名问题）
    kv_file = "app.kv"

    def build(self):
        return GameLayout()


if __name__ == '__main__':
    GuessNumberApp().run()