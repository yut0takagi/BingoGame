import tkinter as tk
import random
import time
from threading import Thread
import pygame
import textwrap

class BingoApp:
    def __init__(self, root):
        self.max_num = 75
        self.root = root
        self.root.title("🎉 ビンゴ大会 🎉")
        self.root.configure(bg="#ffeedd")
        self.root.attributes('-fullscreen', True)  # 全画面モード

        self.called_numbers = set()
        self.remaining_numbers = list(range(1, self.max_num + 1))
        self.shuffling = False

        # pygame mixer 初期化
        pygame.mixer.init()
        self.shuffle_sound = "shuffle_sound.mp3"  # シャッフル音のファイル名

        # メイン番号表示
        self.main_label = tk.Label(
            root,
            text="Let's Bingo!",
            font=("Comic Sans MS", 200, "bold"),  # 大きなフォントサイズ
            fg="#ff5733",
            bg="#ffeedd"
        )
        self.main_label.pack(pady=50, expand=True)

        # 番号履歴表示
        self.history_label = tk.Label(
            root,
            text="番号履歴: ",
            font=("Comic Sans MS", 36),
            bg="#ffeedd",
            fg="#34495e",
            wraplength=1200,  # 折り返し幅
            justify="center"  # 中央揃え
        )
        self.history_label.pack(pady=20, expand=True)

        # ボタンを中央に配置するフレーム
        self.button_frame = tk.Frame(root, bg="#ffeedd")
        self.button_frame.pack(pady=50, expand=True)

        # 次の番号を引くボタン
        self.call_button = tk.Button(
            self.button_frame,
            text="🌟 次の番号を引く 🌟",
            font=("Comic Sans MS", 36, "bold"),
            bg="#85c1e9",
            fg="white",
            command=self.start_shuffling
        )
        self.call_button.pack(side="left", padx=20)

        # リセットボタン
        self.reset_button = tk.Button(
            self.button_frame,
            text="🔄 ゲームをリセット 🔄",
            font=("Comic Sans MS", 36, "bold"),
            bg="#f1948a",
            fg="white",
            command=self.reset_game
        )
        self.reset_button.pack(side="left", padx=20)

        # 名前を表示
        self.fes_label = tk.Label(
            root,
            text="タイトル",
            font=("Comic Sans MS", 36),  # 大きなフォントサイズ
            bg="#ffeedd",
            fg="#34495e"
        )
        self.fes_label.pack(pady=20, expand=True)

        # Escapeキーで全画面を解除するバインド
        self.root.bind("<Escape>", self.exit_fullscreen)

    def start_shuffling(self):
        if self.shuffling or not self.remaining_numbers:
            return
        self.shuffling = True
        self.call_button.config(state="disabled")
        Thread(target=self.shuffle_numbers).start()

    def shuffle_numbers(self):
        pygame.mixer.Sound(self.shuffle_sound).play()  # シャッフル音を再生
        for _ in range(40):
            fake_number = random.randint(1, self.max_num)
            self.main_label.config(text=fake_number, fg="#d35400")
            time.sleep(0.1)
        self.call_number()

    def call_number(self):
        if not self.remaining_numbers:
            self.main_label.config(text="すべての番号が出ました！", fg="#c0392b")
            self.shuffling = False
            return

        # ランダムな番号を引く
        number = random.choice(self.remaining_numbers)
        self.remaining_numbers.remove(number)
        self.called_numbers.add(number)

        # メインラベル更新
        self.main_label.config(text=f"{number}", fg="#27ae60")

        # 番号履歴更新
        self.update_history()

        self.shuffling = False
        self.call_button.config(state="normal")

    def update_history(self):
        # 番号履歴を更新し、折り返しを適用
        history_text = ", ".join(map(str, sorted(self.called_numbers)))
        wrapped_text = textwrap.fill(history_text, width=30)  # 幅30文字ごとに改行
        self.history_label.config(text=f"番号履歴:\n{wrapped_text}")

    def reset_game(self):
        self.called_numbers.clear()
        self.remaining_numbers = list(range(1, self.max_num + 1))
        self.main_label.config(text="Let's Bingo!", fg="#ff5733", font=("Comic Sans MS", 120, "bold"))
        self.history_label.config(text="番号履歴: ")
        self.call_button.config(state="normal")
        self.shuffling = False

    def exit_fullscreen(self, event=None):
        """Escapeキーで全画面を解除"""
        self.root.attributes('-fullscreen', False)
# アプリ起動
if __name__ == "__main__":
    root = tk.Tk()
    app = BingoApp(root)
    root.mainloop()