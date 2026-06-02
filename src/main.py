"""主程序入口 - 启动应用程序"""
import tkinter as tk
from loginView import LoginView
from mainView import MainView


def 启动主界面():
    """登录成功后启动主界面"""
    mainApp = MainView()
    mainApp.运行()


def main():
    """程序主入口"""
    # 创建登录窗口
    loginRoot = tk.Tk()
    LoginView(loginRoot, 启动主界面)
    loginRoot.mainloop()


if __name__ == "__main__":
    main()
