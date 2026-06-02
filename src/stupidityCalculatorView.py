"""傻逼程度计算器界面模块 - 计算傻逼程度"""
import tkinter as tk
from tkinter import messagebox
from utils import centerWindow


class StupidityCalculatorView:
    def __init__(self, parentRoot, onClose):
        self.parentRoot = parentRoot
        self.onClose = onClose
        
        self.window = tk.Toplevel()
        self.window.title("傻逼程度计算器")
        self.window.geometry("500x600")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.关闭窗口)
        
        # 窗口居中
        centerWindow(self.window)
        
        # 题目答案
        self.answers = []
        self.currentQuestion = 0
        self.questions = [
            "1 + 1 = ?",
            "一周有几天？",
            "太阳从哪边升起？",
            "你觉得 TA 有多少概率是傻逼？(0-100)"
        ]
        
        self.创建界面()
    
    def 创建界面(self):
        """创建傻逼程度计算界面"""
        # 标题
        tk.Label(
            self.window,
            text="傻逼程度计算器",
            font=("微软雅黑", 20, "bold"),
            fg="#F44336"
        ).pack(pady=30)
        
        # 说明文字
        tk.Label(
            self.window,
            text="测试别人的傻逼程度",
            font=("微软雅黑", 12),
            fg="#666666"
        ).pack(pady=5)
        
        tk.Label(
            self.window,
            text="让 TA 回答以下问题",
            font=("微软雅黑", 11),
            fg="#999999"
        ).pack(pady=5)
        
        # 问题显示区域
        self.questionFrame = tk.Frame(self.window)
        self.questionFrame.pack(pady=20, padx=40, fill='both', expand=True)
        
        self.显示当前问题()
    
    def 显示当前问题(self):
        """显示当前问题"""
        # 清空问题区域
        for widget in self.questionFrame.winfo_children():
            widget.destroy()
        
        if self.currentQuestion < len(self.questions):
            question = self.questions[self.currentQuestion]
            
            # 问题文本
            tk.Label(
                self.questionFrame,
                text=f"问题 {self.currentQuestion + 1}/{len(self.questions)}",
                font=("微软雅黑", 11),
                fg="#999999"
            ).pack(pady=5)
            
            tk.Label(
                self.questionFrame,
                text=question,
                font=("微软雅黑", 16, "bold"),
                fg="#333333"
            ).pack(pady=20)
            
            # 答案输入框
            self.answerEntry = tk.Entry(
                self.questionFrame,
                font=("微软雅黑", 14),
                width=20,
                justify='center'
            )
            self.answerEntry.pack(pady=20)
            self.answerEntry.focus()
            
            # 提交按钮
            submitButton = tk.Button(
                self.questionFrame,
                text="提交答案" if self.currentQuestion < len(self.questions) - 1 else "查看结果",
                font=("微软雅黑", 13),
                width=15,
                height=2,
                bg="#F44336",
                fg="white",
                command=self.提交答案,
                cursor="hand2"
            )
            submitButton.pack(pady=20)
    
    def 提交答案(self):
        """提交答案"""
        answer = self.answerEntry.get().strip()
        
        if not answer:
            messagebox.showwarning("提示", "请输入答案")
            return
        
        # 保存答案
        self.answers.append(answer)
        self.currentQuestion += 1
        
        # 检查是否完成所有问题
        if self.currentQuestion >= len(self.questions):
            self.计算结果()
        else:
            self.显示当前问题()
    
    def 计算结果(self):
        """计算傻逼程度"""
        # 前面的题目答案全部 * 0
        # 最后一题答案作为概率
        try:
            lastAnswer = float(self.answers[-1])
            # 确保在 0-100 范围内
            probability = max(0, min(100, lastAnswer))
        except ValueError:
            # 如果最后一题输入无效，默认为 50
            probability = 50
        
        messagebox.showinfo(
            "计算结果",
            f"经过科学计算分析\n\nTA 有 {probability:.0f}% 的概率是傻逼！"
        )
        self.关闭并返回()
    
    def 关闭窗口(self):
        """关闭窗口"""
        self.关闭并返回()
    
    def 关闭并返回(self):
        """关闭当前窗口并返回主界面"""
        self.window.destroy()
        self.onClose()
