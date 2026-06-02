"""密码管理模块 - 负责密码的加密存储和验证"""
import hashlib
import json
import os


class PasswordManager:
    def __init__(self, configFile='config.json'):
        self.configFile = configFile
        self.passwordData = None
    
    def 加载配置(self):
        """从配置文件加载密码数据"""
        if os.path.exists(self.configFile):
            with open(self.configFile, 'r', encoding='utf-8') as f:
                self.passwordData = json.load(f)
            return True
        return False
    
    def 保存密码(self, passwordStr):
        """保存密码（MD5加密）"""
        passwordMd5 = hashlib.md5(passwordStr.encode()).hexdigest()
        self.passwordData = {
            'password': passwordMd5,
            'passwordLength': len(passwordStr),
            'passwordPlain': passwordStr  # 用于验证位数
        }
        with open(self.configFile, 'w', encoding='utf-8') as f:
            json.dump(self.passwordData, f, ensure_ascii=False)
    
    def 验证密码位(self, position, digit):
        """验证指定位置的密码数字是否正确"""
        if self.passwordData is None:
            return False
        
        plainPassword = self.passwordData.get('passwordPlain', '')
        if position < 0 or position >= len(plainPassword):
            return False
        
        return plainPassword[position] == str(digit)
    
    def 是否首次使用(self):
        """检查是否首次使用"""
        return not self.加载配置()
    
    def 获取密码长度(self):
        """获取密码长度"""
        if self.passwordData:
            return self.passwordData.get('passwordLength', 0)
        return 0
