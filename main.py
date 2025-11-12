import server
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

if __name__ == '__main__':
    server.start_server()
