from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
import random

# 设置窗口大小（仅桌面调试用，手机上会自适应）
Window.size = (300, 400)

class GuessNumberGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(** kwargs)
        self.orientation = 'vertical'  # 垂直布局
        self.padding = 20  # 内边距
        self.spacing = 15  # 控件间距
        
        # 生成1-100之间的随机数
        self.target_number = random.randint(1, 100)
        self.guess_count = 0  # 记录猜测次数
        
        # 添加标题
        self.title_label = Label(
            text="猜数字游戏",
            font_size=24,
            size_hint_y=None,
            height=50
        )
        self.add_widget(self.title_label)
        
        # 添加提示信息
        self.info_label = Label(
            text="请输入1-100之间的数字：",
            font_size=16,
            size_hint_y=None,
            height=40
        )
        self.add_widget(self.info_label)
        
        # 添加输入框
        self.input = TextInput(
            input_type='number',  # 仅允许数字输入
            font_size=18,
            size_hint_y=None,
            height=40
        )
        self.add_widget(self.input)
        
        # 添加提交按钮
        self.submit_btn = Button(
            text="提交猜测",
            background_color=(0.2, 0.6, 1, 1),  # 蓝色
            font_size=18,
            size_hint_y=None,
            height=50
        )
        self.submit_btn.bind(on_press=self.check_guess)  # 绑定点击事件
        self.add_widget(self.submit_btn)
        
        # 添加结果显示
        self.result_label = Label(
            text="",
            font_size=16,
            size_hint_y=None,
            height=40
        )
        self.add_widget(self.result_label)
        
        # 添加重置按钮
        self.reset_btn = Button(
            text="重新开始",
            background_color=(1, 0.4, 0.4, 1),  # 浅红色
            font_size=18,
            size_hint_y=None,
            height=50
        )
        self.reset_btn.bind(on_press=self.reset_game)  # 绑定点击事件
        self.add_widget(self.reset_btn)

    def check_guess(self, instance):
        """检查用户猜测的数字"""
        try:
            # 获取用户输入并转换为整数
            guess = int(self.input.text.strip())
            self.guess_count += 1  # 次数+1
            
            # 判断大小
            if guess < 1 or guess > 100:
                self.result_label.text = "请输入1-100之间的数字！"
            elif guess < self.target_number:
                self.result_label.text = f"猜小了！已猜{self.guess_count}次"
            elif guess > self.target_number:
                self.result_label.text = f"猜大了！已猜{self.guess_count}次"
            else:
                # 猜对了
                self.result_label.text = f"恭喜猜对了！共猜了{self.guess_count}次"
        except ValueError:
            # 输入非数字时提示
            self.result_label.text = "请输入有效的数字！"
        
        # 清空输入框
        self.input.text = ""

    def reset_game(self, instance):
        """重置游戏"""
        self.target_number = random.randint(1, 100)
        self.guess_count = 0
        self.info_label.text = "请输入1-100之间的数字："
        self.result_label.text = ""
        self.input.text = ""

class GuessNumberApp(App):
    def build(self):
        return GuessNumberGame()

if __name__ == "__main__":
    GuessNumberApp().run()
