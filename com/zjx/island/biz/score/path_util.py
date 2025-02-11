import os
import sys
from pathlib import Path

def get_app_path():
    """获取 .app 文件所在的根目录"""
    if hasattr(sys, '_MEIPASS'):
        # 获取当前可执行文件的目录
        app_dir = Path(sys.executable).resolve().parent
        # 检测 macOS .app 文件的结构，将路径回溯到 .app 的根目录
        if app_dir.name == "MacOS":
            return app_dir.parent.parent.parent  # 返回到 .app 的根目录
        return app_dir
    else:
        # 普通 Python 脚本运行
        return Path(__file__).resolve().parent

def get_config_path(subfolder, filename):
    # 获取基路径：打包后使用 _MEIPASS
    if hasattr(sys, "_MEIPASS"):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).resolve().parent

    # 返回子文件夹中的配置文件路径
    return base_path / subfolder / filename


def create_results_folder(folder_name="results"):
    """
    在当前运行目录下创建一个文件夹来存储结果文件
    """
    # 获取当前运行目录
    current_working_dir = get_app_path()

    # 构造结果文件夹路径
    results_folder = current_working_dir / folder_name

    # 创建文件夹（如果不存在）
    results_folder.mkdir(parents=True, exist_ok=True)
    print(f"结果文件夹已创建: {results_folder}")

    return results_folder
