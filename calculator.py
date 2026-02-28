import tkinter as tk
from tkinter import ttk

class SpeedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("阴阳师速度计算器")
        self.root.geometry("700x700")
        self.root.resizable(False, False)
        
        # 设置样式
        style = ttk.Style()
        style.configure('TLabel', font=('微软雅黑', 10))
        style.configure('TEntry', font=('微软雅黑', 10))
        style.configure('Title.TLabel', font=('微软雅黑', 14, 'bold'))
        style.configure('Result.TLabel', font=('微软雅黑', 11), foreground='blue')
        style.configure('Formula.TLabel', font=('微软雅黑', 9), foreground='gray')
        style.configure('CalcButton.TButton', font=('微软雅黑', 10, 'bold'))
        
        # 主容器
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky="nwes")
        
        # ==================== 白葛计算器 ====================
        title1 = ttk.Label(main_frame, text="白葛计算器", style='Title.TLabel')
        title1.grid(row=0, column=0, columnspan=4, pady=(0, 10), sticky=tk.W)
        
        # 公式说明
        formula_text = "公式: 白藏主实际 × (葛叶实际 + 75) / (75 + 白藏主实际) = 阎魔实际"
        formula_label = ttk.Label(main_frame, text=formula_text, style='Formula.TLabel')
        formula_label.grid(row=1, column=0, columnspan=4, pady=(0, 10), sticky=tk.W)
        
        # 基础速度说明
        base_text = "基础: 葛叶=117 白藏主=171 阎魔=127"
        base_label = ttk.Label(main_frame, text=base_text, style='Formula.TLabel')
        base_label.grid(row=2, column=0, columnspan=4, pady=(0, 15), sticky=tk.W)
        
        # 计算模式选择
        ttk.Label(main_frame, text="已知条件:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.baige_mode = ttk.Combobox(main_frame, values=[
            "葛叶御魂速度 + 白藏主御魂速度",
            "葛叶御魂速度 + 阎魔御魂速度", 
            "白藏主御魂速度 + 阎魔御魂速度"
        ], width=28, state="readonly")
        self.baige_mode.grid(row=3, column=1, columnspan=2, padx=5, pady=5, sticky=tk.W)
        self.baige_mode.current(0)
        self.baige_mode.bind('<<ComboboxSelected>>', self.on_baige_mode_change)
        
        # 输入框1
        ttk.Label(main_frame, text="速度 1:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.baige_input1 = ttk.Entry(main_frame, width=15)
        self.baige_input1.grid(row=4, column=1, padx=5, pady=5)
        self.baige_label1 = ttk.Label(main_frame, text="葛叶御魂速度")
        self.baige_label1.grid(row=4, column=2, padx=5, pady=5, sticky=tk.W)
        
        # 输入框2
        ttk.Label(main_frame, text="速度 2:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.baige_input2 = ttk.Entry(main_frame, width=15)
        self.baige_input2.grid(row=5, column=1, padx=5, pady=5)
        self.baige_label2 = ttk.Label(main_frame, text="白藏主御魂速度")
        self.baige_label2.grid(row=5, column=2, padx=5, pady=5, sticky=tk.W)
        
        # 计算按钮
        calc_btn1 = ttk.Button(main_frame, text="计算", command=self.calculate_baige, style='CalcButton.TButton')
        calc_btn1.grid(row=4, column=3, rowspan=2, padx=10, pady=5)
        
        # 结果显示
        ttk.Label(main_frame, text="计算结果:").grid(row=6, column=0, sticky=tk.W, pady=10)
        self.baige_result = ttk.Label(main_frame, text="--", font=('微软雅黑', 12, 'bold'), foreground='red')
        self.baige_result.grid(row=6, column=1, columnspan=3, padx=5, pady=10, sticky=tk.W)
        
        # 详细信息
        self.baige_detail = ttk.Label(main_frame, text="", style='Result.TLabel')
        self.baige_detail.grid(row=7, column=0, columnspan=4, padx=5, pady=5, sticky=tk.W)
        
        # 分隔线
        ttk.Separator(main_frame, orient='horizontal').grid(row=8, column=0, columnspan=4, sticky="we", pady=15)
        
        # ==================== 白面计算器 ====================
        title2 = ttk.Label(main_frame, text="白面计算器", style='Title.TLabel')
        title2.grid(row=9, column=0, columnspan=4, pady=(0, 10), sticky=tk.W)
        
        # 公式说明
        formula_text2 = "公式: 白藏主实际 × (面灵气实际 + 60) / (60 + 白藏主实际) = 阎魔实际"
        formula_label2 = ttk.Label(main_frame, text=formula_text2, style='Formula.TLabel')
        formula_label2.grid(row=10, column=0, columnspan=4, pady=(0, 10), sticky=tk.W)
        
        # 基础速度说明
        base_text2 = "基础: 面灵气=119 白藏主=171 阎魔=127"
        base_label2 = ttk.Label(main_frame, text=base_text2, style='Formula.TLabel')
        base_label2.grid(row=11, column=0, columnspan=4, pady=(0, 15), sticky=tk.W)
        
        # 计算模式选择
        ttk.Label(main_frame, text="已知条件:").grid(row=12, column=0, sticky=tk.W, pady=5)
        self.baimian_mode = ttk.Combobox(main_frame, values=[
            "面灵气御魂速度 + 白藏主御魂速度",
            "面灵气御魂速度 + 阎魔御魂速度",
            "白藏主御魂速度 + 阎魔御魂速度"
        ], width=28, state="readonly")
        self.baimian_mode.grid(row=12, column=1, columnspan=2, padx=5, pady=5, sticky=tk.W)
        self.baimian_mode.current(0)
        self.baimian_mode.bind('<<ComboboxSelected>>', self.on_baimian_mode_change)
        
        # 输入框1
        ttk.Label(main_frame, text="速度 1:").grid(row=13, column=0, sticky=tk.W, pady=5)
        self.baimian_input1 = ttk.Entry(main_frame, width=15)
        self.baimian_input1.grid(row=13, column=1, padx=5, pady=5)
        self.baimian_label1 = ttk.Label(main_frame, text="面灵气御魂速度")
        self.baimian_label1.grid(row=13, column=2, padx=5, pady=5, sticky=tk.W)
        
        # 输入框2
        ttk.Label(main_frame, text="速度 2:").grid(row=14, column=0, sticky=tk.W, pady=5)
        self.baimian_input2 = ttk.Entry(main_frame, width=15)
        self.baimian_input2.grid(row=14, column=1, padx=5, pady=5)
        self.baimian_label2 = ttk.Label(main_frame, text="白藏主御魂速度")
        self.baimian_label2.grid(row=14, column=2, padx=5, pady=5, sticky=tk.W)
        
        # 计算按钮
        calc_btn2 = ttk.Button(main_frame, text="计算", command=self.calculate_baimian, style='CalcButton.TButton')
        calc_btn2.grid(row=13, column=3, rowspan=2, padx=10, pady=5)
        
        # 结果显示
        ttk.Label(main_frame, text="计算结果:").grid(row=15, column=0, sticky=tk.W, pady=10)
        self.baimian_result = ttk.Label(main_frame, text="--", font=('微软雅黑', 12, 'bold'), foreground='red')
        self.baimian_result.grid(row=15, column=1, columnspan=3, padx=5, pady=10, sticky=tk.W)
        
        # 详细信息
        self.baimian_detail = ttk.Label(main_frame, text="", style='Result.TLabel')
        self.baimian_detail.grid(row=16, column=0, columnspan=4, padx=5, pady=5, sticky=tk.W)
        
        # 说明文字
        note_text = "说明: 输入御魂速度（不是实际速度），点击计算得出第三个御魂速度。结果保留4位小数。"
        note_label = ttk.Label(main_frame, text=note_text, font=('微软雅黑', 9), foreground='gray')
        note_label.grid(row=17, column=0, columnspan=4, pady=(20, 0), sticky=tk.W)
    
    def on_baige_mode_change(self, event=None):
        """白葛模式改变时更新标签"""
        mode = self.baige_mode.current()
        if mode == 0:  # 葛叶 + 白藏主
            self.baige_label1.config(text="葛叶御魂速度")
            self.baige_label2.config(text="白藏主御魂速度")
        elif mode == 1:  # 葛叶 + 阎魔
            self.baige_label1.config(text="葛叶御魂速度")
            self.baige_label2.config(text="阎魔御魂速度")
        else:  # 白藏主 + 阎魔
            self.baige_label1.config(text="白藏主御魂速度")
            self.baige_label2.config(text="阎魔御魂速度")
        self.baige_result.config(text="--")
        self.baige_detail.config(text="")
    
    def on_baimian_mode_change(self, event=None):
        """白面模式改变时更新标签"""
        mode = self.baimian_mode.current()
        if mode == 0:  # 面灵气 + 白藏主
            self.baimian_label1.config(text="面灵气御魂速度")
            self.baimian_label2.config(text="白藏主御魂速度")
        elif mode == 1:  # 面灵气 + 阎魔
            self.baimian_label1.config(text="面灵气御魂速度")
            self.baimian_label2.config(text="阎魔御魂速度")
        else:  # 白藏主 + 阎魔
            self.baimian_label1.config(text="白藏主御魂速度")
            self.baimian_label2.config(text="阎魔御魂速度")
        self.baimian_result.config(text="--")
        self.baimian_detail.config(text="")
    
    def calculate_baige(self):
        """计算白葛"""
        try:
            mode = self.baige_mode.current()
            val1 = float(self.baige_input1.get()) if self.baige_input1.get() else 0
            val2 = float(self.baige_input2.get()) if self.baige_input2.get() else 0
            
            # 基础速度
            GEYE_BASE = 117
            BAIZANG_BASE = 111 + 60  # 171
            YANMO_BASE = 127
            
            if mode == 0:  # 已知葛叶御魂(G)和白藏主御魂(B)，求阎魔御魂(Y)
                # G_实际 = G + 117, B_实际 = B + 171
                # Y_实际 = B_实际 × (G_实际 + 75) / (75 + B_实际)
                # Y_御魂 = Y_实际 - 127
                G, B = val1, val2
                G_actual = G + GEYE_BASE
                B_actual = B + BAIZANG_BASE
                
                if B_actual <= 0:
                    self.baige_result.config(text="错误: 白藏主实际速度必须大于0")
                    return
                    
                Y_actual = B_actual * (G_actual + 75) / (75 + B_actual)
                Y = Y_actual - YANMO_BASE
                
                self.baige_result.config(text=f"阎魔御魂速度: {Y:.4f}")
                self.baige_detail.config(text=f"葛叶实际={G_actual:.4f}, 白藏主实际={B_actual:.4f}, 阎魔实际={Y_actual:.4f}")
                
            elif mode == 1:  # 已知葛叶御魂(G)和阎魔御魂(Y)，求白藏主御魂(B)
                # 从公式推导: B_实际 = 75 × Y_实际 / (G_实际 + 75 - Y_实际)
                G, Y = val1, val2
                G_actual = G + GEYE_BASE
                Y_actual = Y + YANMO_BASE
                
                denominator = G_actual + 75 - Y_actual
                if denominator <= 0:
                    self.baige_result.config(text="错误: 输入值不合法(分母必须>0)")
                    return
                    
                B_actual = 75 * Y_actual / denominator
                B = B_actual - BAIZANG_BASE
                
                self.baige_result.config(text=f"白藏主御魂速度: {B:.4f}")
                self.baige_detail.config(text=f"葛叶实际={G_actual:.4f}, 白藏主实际={B_actual:.4f}, 阎魔实际={Y_actual:.4f}")
                
            else:  # 已知白藏主御魂(B)和阎魔御魂(Y)，求葛叶御魂(G)
                # 从公式推导: G_实际 = (Y_实际 × (75 + B_实际) - 75 × B_实际) / B_实际
                B, Y = val1, val2
                B_actual = B + BAIZANG_BASE
                Y_actual = Y + YANMO_BASE
                
                if B_actual <= 0:
                    self.baige_result.config(text="错误: 白藏主实际速度必须大于0")
                    return
                    
                G_actual = (Y_actual * (75 + B_actual) - 75 * B_actual) / B_actual
                G = G_actual - GEYE_BASE
                
                self.baige_result.config(text=f"葛叶御魂速度: {G:.4f}")
                self.baige_detail.config(text=f"葛叶实际={G_actual:.4f}, 白藏主实际={B_actual:.4f}, 阎魔实际={Y_actual:.4f}")
                
        except ValueError:
            self.baige_result.config(text="错误: 请输入有效数字")
        except ZeroDivisionError:
            self.baige_result.config(text="错误: 除数不能为零")
    
    def calculate_baimian(self):
        """计算白面"""
        try:
            mode = self.baimian_mode.current()
            val1 = float(self.baimian_input1.get()) if self.baimian_input1.get() else 0
            val2 = float(self.baimian_input2.get()) if self.baimian_input2.get() else 0
            
            # 基础速度
            MIANLING_BASE = 119
            BAIZANG_BASE = 111 + 60  # 171
            YANMO_BASE = 127
            
            if mode == 0:  # 已知面灵气御魂(M)和白藏主御魂(B)，求阎魔御魂(Y)
                # M_实际 = M + 119, B_实际 = B + 171
                # Y_实际 = B_实际 × (M_实际 + 60) / (60 + B_实际)
                # Y_御魂 = Y_实际 - 127
                M, B = val1, val2
                M_actual = M + MIANLING_BASE
                B_actual = B + BAIZANG_BASE
                
                if B_actual <= 0:
                    self.baimian_result.config(text="错误: 白藏主实际速度必须大于0")
                    return
                    
                Y_actual = B_actual * (M_actual + 60) / (60 + B_actual)
                Y = Y_actual - YANMO_BASE
                
                self.baimian_result.config(text=f"阎魔御魂速度: {Y:.4f}")
                self.baimian_detail.config(text=f"面灵气实际={M_actual:.4f}, 白藏主实际={B_actual:.4f}, 阎魔实际={Y_actual:.4f}")
                
            elif mode == 1:  # 已知面灵气御魂(M)和阎魔御魂(Y)，求白藏主御魂(B)
                # 从公式推导: B_实际 = 60 × Y_实际 / (M_实际 + 60 - Y_实际)
                M, Y = val1, val2
                M_actual = M + MIANLING_BASE
                Y_actual = Y + YANMO_BASE
                
                denominator = M_actual + 60 - Y_actual
                if denominator <= 0:
                    self.baimian_result.config(text="错误: 输入值不合法(分母必须>0)")
                    return
                    
                B_actual = 60 * Y_actual / denominator
                B = B_actual - BAIZANG_BASE
                
                self.baimian_result.config(text=f"白藏主御魂速度: {B:.4f}")
                self.baimian_detail.config(text=f"面灵气实际={M_actual:.4f}, 白藏主实际={B_actual:.4f}, 阎魔实际={Y_actual:.4f}")
                
            else:  # 已知白藏主御魂(B)和阎魔御魂(Y)，求面灵气御魂(M)
                # 从公式推导: M_实际 = (Y_实际 × (60 + B_实际) - 60 × B_实际) / B_实际
                B, Y = val1, val2
                B_actual = B + BAIZANG_BASE
                Y_actual = Y + YANMO_BASE
                
                if B_actual <= 0:
                    self.baimian_result.config(text="错误: 白藏主实际速度必须大于0")
                    return
                    
                M_actual = (Y_actual * (60 + B_actual) - 60 * B_actual) / B_actual
                M = M_actual - MIANLING_BASE
                
                self.baimian_result.config(text=f"面灵气御魂速度: {M:.4f}")
                self.baimian_detail.config(text=f"面灵气实际={M_actual:.4f}, 白藏主实际={B_actual:.4f}, 阎魔实际={Y_actual:.4f}")
                
        except ValueError:
            self.baimian_result.config(text="错误: 请输入有效数字")
        except ZeroDivisionError:
            self.baimian_result.config(text="错误: 除数不能为零")

def main():
    root = tk.Tk()
    app = SpeedCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
