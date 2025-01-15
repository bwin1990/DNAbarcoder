from typing import List
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from rpy2.rinterface_lib.embedded import RRuntimeError
import os

class RInterface:
    def __init__(self):
        """初始化R接口"""
        # 加载R脚本
        self.r_script_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            'r_scripts',
            'generate_barcodes.R'
        )
        robjects.r.source(self.r_script_path)
        
    def generate_barcodes(self, length: int, n: int, dist: int) -> List[str]:
        """
        生成DNA条形码序列
        
        Args:
            length: 条形码长度
            n: 需要生成的条形码数量
            dist: 最小汉明距离
            
        Returns:
            List[str]: 条形码序列列表
        """
        r_generate = robjects.r['generate_dna_barcodes']
        try:
            r_barcodes = r_generate(length, n, dist)
        except RRuntimeError as e:
            # 捕获 R 脚本抛出的错误，并包装成更直观的 Python 异常
            raise RuntimeError(
                f"R 端生成条形码时出错，请检查参数（长度={length} / 数量={n} / 最小距离={dist}）是否合理：\n{e}"
            ) from e
        
        return list(r_barcodes)
    
    def save_barcodes(self, barcodes: List[str], filepath: str) -> None:
        """
        保存条形码序列到文件
        
        Args:
            barcodes: 条形码序列列表
            filepath: 输出文件路径
        """
        r_save = robjects.r['save_barcodes']
        r_barcodes = robjects.StrVector(barcodes)
        try:
            r_save(r_barcodes, filepath)
        except RRuntimeError as e:
            raise RuntimeError(
                f"R 端保存条形码文件出错，请检查输出路径是否可写或参数合法性：\n{e}"
            ) from e 