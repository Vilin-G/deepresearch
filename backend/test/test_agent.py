from agent.base_agent import *
import os

# 密钥一律走环境变量，不要写进代码（本地可放 backend/.env，模板见 backend/.env.example）：
#   APP_TOKEN / APP_ID / GEMINI_API_KEY
os.environ.setdefault('LLM_BASE_URL', 'https://dashscope.aliyuncs.com/compatible-mode/v1')

if __name__ == '__main__':
    agent = Agent()
    response = agent("中国的首都是那里？")
