"""工具函数模块 - 提供通用功能函数"""


def centerWindow(window):
    """将窗口居中显示在屏幕中央"""
    window.update_idletasks()
    
    # 获取窗口尺寸
    windowWidth = window.winfo_width()
    windowHeight = window.winfo_height()
    
    # 获取屏幕尺寸
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    
    # 计算居中位置
    x = (screenWidth - windowWidth) // 2
    y = (screenHeight - windowHeight) // 2
    
    # 设置窗口位置
    window.geometry(f"{windowWidth}x{windowHeight}+{x}+{y}")
