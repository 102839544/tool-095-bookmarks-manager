#!/usr/bin/env python3
"""
bookmarks-manager - 书签管理工具
工具编号: tool-095
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import random

class App:
    def __init__(self, root):
        self.root = root
        root.title("书签管理工具 v1.0")
        root.geometry("700x500")
        self.setup_ui()
    
    def setup_ui(self):
        # 标题
        title_frame = tk.Frame(self.root, bg="#009688", height=60)
        title_frame.pack(fill="x")
        title_frame.pack_propagate(False)
        tk.Label(title_frame, text="📦 书签管理工具", font=("Arial", 18, "bold"),
                 fg="white", bg="#009688").pack(pady=15)
        
        # 主区域
        main = tk.Frame(self.root, padx=30, pady=20)
        main.pack(fill="both", expand=True)
        
        # 根据工具名称添加特定功能
        if "timer" in "bookmarks-manager".lower() or "clock" in "bookmarks-manager".lower():
            self.setup_timer_ui(main)
        elif "random" in "bookmarks-manager".lower() or "dice" in "bookmarks-manager".lower() or "coin" in "bookmarks-manager".lower():
            self.setup_random_ui(main)
        elif "note" in "bookmarks-manager".lower() or "todo" in "bookmarks-manager".lower():
            self.setup_note_ui(main)
        else:
            self.setup_generic_ui(main)
        
        # 状态栏
        self.status_var = tk.StringVar(value="就绪")
        tk.Label(main, textvariable=self.status_var, fg="gray").pack(fill="x", pady=10)
    
    def setup_timer_ui(self, parent):
        # 时间显示
        self.time_label = tk.Label(parent, text="00:00:00", font=("Arial", 48, "bold"))
        self.time_label.pack(pady=30)
        
        # 按钮
        btn_frame = tk.Frame(parent)
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="▶️ 开始", command=self.start_timer,
                  bg="#4CAF50", fg="white", font=("Arial", 12), padx=20, pady=10).pack(side="left", padx=10)
        tk.Button(btn_frame, text="⏸️ 暂停", command=self.pause_timer,
                  bg="#FF9800", fg="white", font=("Arial", 12), padx=20, pady=10).pack(side="left", padx=10)
        tk.Button(btn_frame, text="🔄 重置", command=self.reset_timer,
                  bg="#f44336", fg="white", font=("Arial", 12), padx=20, pady=10).pack(side="left", padx=10)
        
        self.running = False
        self.seconds = 0
        self.update_timer()
    
    def start_timer(self):
        self.running = True
        self.status_var.set("计时中...")
    
    def pause_timer(self):
        self.running = False
        self.status_var.set("已暂停")
    
    def reset_timer(self):
        self.running = False
        self.seconds = 0
        self.time_label.config(text="00:00:00")
        self.status_var.set("已重置")
    
    def update_timer(self):
        if self.running:
            self.seconds += 1
            h = self.seconds // 3600
            m = (self.seconds % 3600) // 60
            s = self.seconds % 60
            self.time_label.config(text=f"{h:02d}:{m:02d}:{s:02d}")
        self.root.after(1000, self.update_timer)
    
    def setup_random_ui(self, parent):
        # 结果显示
        self.result_label = tk.Label(parent, text="点击按钮生成", font=("Arial", 36, "bold"))
        self.result_label.pack(pady=40)
        
        # 按钮
        btn_frame = tk.Frame(parent)
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="🎲 随机生成", command=self.generate_random,
                  bg="#9C27B0", fg="white", font=("Arial", 14, "bold"),
                  padx=40, pady=15).pack(pady=20)
    
    def generate_random(self):
        if "dice" in "bookmarks-manager".lower():
            result = random.randint(1, 6)
            self.result_label.config(text=f"🎲 {result}")
        elif "coin" in "bookmarks-manager".lower():
            result = random.choice(["正面", "反面"])
            self.result_label.config(text=f"🪙 {result}")
        else:
            result = random.randint(1, 100)
            self.result_label.config(text=str(result))
        self.status_var.set("✅ 已生成")
    
    def setup_note_ui(self, parent):
        # 输入区
        tk.Label(parent, text="📝 输入内容:", font=("Arial", 10, "bold")).pack(anchor="w")
        self.note_entry = tk.Text(parent, font=("Arial", 11), height=10)
        self.note_entry.pack(fill="both", expand=True, pady=10)
        
        # 按钮
        btn_frame = tk.Frame(parent)
        btn_frame.pack(fill="x")
        
        tk.Button(btn_frame, text="💾 保存", command=self.save_note,
                  bg="#4CAF50", fg="white", padx=20, pady=8).pack(side="left", padx=5)
        tk.Button(btn_frame, text="🗑️ 清空", command=self.clear_note,
                  bg="#f44336", fg="white", padx=20, pady=8).pack(side="left", padx=5)
    
    def save_note(self):
        self.status_var.set("✅ 已保存")
        messagebox.showinfo("保存", "笔记已保存")
    
    def clear_note(self):
        self.note_entry.delete(1.0, tk.END)
        self.status_var.set("已清空")
    
    def setup_generic_ui(self, parent):
        tk.Label(parent, text="🔧 功能开发中...", font=("Arial", 16)).pack(pady=50)
        tk.Button(parent, text="开始使用", command=lambda: messagebox.showinfo("提示", "功能开发中"),
                  bg="#4CAF50", fg="white", padx=30, pady=15).pack(pady=20)

def main():
    root = tk.Tk()
    App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
