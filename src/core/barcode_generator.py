from typing import List
from ..utils.r_interface import RInterface

class BarcodeGenerator:
    def __init__(self):
        """初始化条形码生成器"""
        self.r_interface = RInterface()
    
    def generate(self, length: int, n: int, dist: int) -> List[str]:
        """
        生成DNA条形码
        
        Args:
            length: 条形码长度
            n: 需要生成的条形码数量
            dist: 最小汉明距离
            
        Returns:
            List[str]: 生成的条形码序列列表
        """
        # 参数验证
        if length < 1:
            raise ValueError("条形码长度必须大于0")
        if n < 1:
            raise ValueError("条形码数量必须大于0")
        if dist < 1:
            raise ValueError("最小距离必须大于0")
            
        return self.r_interface.generate_barcodes(length, n, dist)
    
    def save_to_file(self, barcodes: List[str], filepath: str) -> None:
        """
        保存条形码到文件
        
        Args:
            barcodes: 条形码序列列表
            filepath: 输出文件路径
        """
        self.r_interface.save_barcodes(barcodes, filepath) 