import logging
import sys
import asyncio
import argparse
from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent
from .schemas.rag import RAGQuery
from .service import RAGService
from .config import config

# 配置日志
if config.RAG_ENABLE_LOGGING:
    logging.basicConfig(
        level=getattr(logging, config.RAG_LOG_LEVEL),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
logger = logging.getLogger(__name__)

# 创建FastMCP服务器实例
mcp = FastMCP("rag-mcp-server")

@mcp.tool(name="rag_search", description="搜索文档，使用语义搜索或关键词搜索")
async def rag_search(
    query: str,
    top_k: int = 10,
    query_type: str = "semanticSearch",
    filter: Optional[Dict[str, Any]] = None,
    rerank: bool = False,
    rerank_model: Optional[str] = None
) -> str:
    """
    搜索文档，使用语义搜索或关键词搜索
    
    Args:
        query: 查询内容
        top_k: 返回结果数量
        query_type: 查询类型
        filter: 过滤条件
        rerank: 是否重新排序
        rerank_model: 重新排序模型
    
    Returns:
        搜索结果
    """
    try:
        logger.info(f"收到搜索请求: {query}")
        
        # 构建RAGQuery对象
        rag_query = RAGQuery(
            query=query,
            top_k=top_k,
            query_type=query_type,
            filter=filter or {},
            rerank=rerank,
            rerank_model=rerank_model
        )
        
        # 调用RAG服务
        result = await RAGService.search(rag_query)
        
        logger.info("搜索完成")
        
        # 返回结果
        return f"搜索完成，找到文档：{result.id}\n内容：{result.content[:200]}...\n元数据：{result.metadata}"
        
    except Exception as e:
        logger.error(f"搜索失败: {e}")
        raise

def run():
    """主函数，支持命令行参数"""
    parser = argparse.ArgumentParser(description="RAG MCP Server")
    parser.add_argument("--port", type=int, default=8080, help="服务器端口")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="服务器主机")
    parser.add_argument("--transport", type=str, choices=["stdio", "sse", "streamable-http"], default="stdio", help="传输方式")
    parser.add_argument("--mount-path", type=str, default="/mcp", help="SSE挂载路径")
    
    args = parser.parse_args()
    
    try:
        if args.transport == "sse":
            # SSE传输模式
            logger.info(f"启动SSE服务器在 {args.host}:{args.port}")
            # 配置服务器设置
            mcp.settings.port = args.port
            mcp.settings.host = args.host
            
            # 启动SSE服务器
            mcp.run(transport="sse", mount_path=args.mount_path)
            
        elif args.transport == "streamable-http":
            # HTTP传输模式
            logger.info(f"启动HTTP服务器在 {args.host}:{args.port}")
            mcp.settings.port = args.port
            mcp.settings.host = args.host
            mcp.run(transport="streamable-http", mount_path=args.mount_path)
            
        else:
            # stdio传输模式（默认）
            logger.info("启动stdio服务器")
            mcp.run(transport="stdio")
            
    except Exception as e:
        logger.error(f"启动服务器失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run()