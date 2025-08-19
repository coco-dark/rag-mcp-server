#!/usr/bin/env python3
"""
启动脚本 - 用于运行 RAG MCP 服务器
"""
import sys
import os
import argparse

# 添加src目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def main():
    """主函数"""
    # 导入并运行服务器
    from src.rag_mcp_server_lizhibing.server import run
    
    run()

if __name__ == "__main__":
    main() 