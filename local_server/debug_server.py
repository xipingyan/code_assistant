import socketserver
import json
import random
import time
from datetime import datetime

# ----------------------------------------------------
# Server 配置
# ----------------------------------------------------
HOST = "127.0.0.1"
PORT = 8080

# ----------------------------------------------------
# 模拟代码生成的内容
# ----------------------------------------------------
def generate_mock_code_generate(prompt: str, language: str) -> str:
    """根据接收到的 prompt 和语言生成一段模拟代码。"""
    
    if language == 'python':
        code_example = f"""
def generated_function_by_ai(input_data):
    # 根据您的 prompt: '{prompt}' 生成
    print(f"Processing input in Python: {{input_data}}")
    # 模拟复杂的逻辑
    result = sum(range(100)) + random.randint(1, 10)
    return f"Result is {{result}} at {{datetime.now().strftime('%H:%M:%S')}}"
"""
    elif language == 'typescript' or language == 'javascript':
        code_example = f"""
// AI Generated Code based on prompt: '{prompt}'
function generatedFunctionByAI(data: any): string {{
    console.log(`Processing input in {{data}} at ${{new Date().toLocaleTimeString()}}`);
    // Simulate some logic
    const result = Math.floor(Math.random() * 1000) + 1;
    return `The generated result is: ${{result}}`;
}}
"""
    elif language == 'cpp' or language == 'c':
        code_example = f"""
// AI Generated Code based on prompt: '{prompt}'
for (size_t i = 0; i < 20; i++) {{
    // here is your code.
}}
"""
    else:
        # 默认返回一些通用文本
        code_example = f"// AI response for language '{language}' (Prompt: '{prompt}').\n// Hello from your OpenVINO Local Server Mock!\n// Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"

    return code_example.strip()

def generate_mock_code_edit(prompt: str, language: str, original_codes: str) -> str:
    """根据接收到的 prompt 和语言生成一段模拟代码。"""
    
    if language == 'cpp' or language == 'c':
        code_example = f"""
// AI Refactor Code based on prompt: '{prompt}'
int r = 10 + 20;
"""
    else:
        # 默认返回一些通用文本
        code_example = f"// AI response for language '{language}' (Prompt: '{prompt}').\n// Hello from your OpenVINO Local Server Mock!\n// Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"

    return code_example.strip()

# ----------------------------------------------------
# TCP 请求处理程序
# ----------------------------------------------------
class AIServerHandler(socketserver.BaseRequestHandler):
    """
    处理传入的 TCP 请求，接收数据，生成模拟响应，并返回。
    """
    def handle(self):
        print("\n" + "="*50)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] New connection from {self.client_address[0]}:{self.client_address[1]}")
        client_name = f"{self.client_address[0]}:{self.client_address[1]}"
        
        self.data = b""
        try:
            # 接收所有数据，直到连接关闭
            while True:
                chunk = self.request.recv(1024)
                if not chunk:
                    break
                self.data += chunk
            
            if not self.data:
                print(f"  client[{client_name}]: Received empty data.")
                return
            
            received_data = self.data.decode('utf-8').strip()
            print(f"  client[{client_name}]:Received data:\n  {received_data}")
            
            # 尝试解析 JSON
            try:
                request_json = json.loads(received_data)
                type = request_json.get('type', 'Default Prompt')
                prompt = request_json.get('prompt', 'Default Prompt')
                language = request_json.get('language', 'unknown')
                original_codes = request_json.get('original_codes', 'unknown')
                print(f"  Parsed Request:")
                print(f"      Type: {type}")
                print(f"      Language: {language}")
                print(f"      Prompt: {prompt[:50]}...")
                print(f"      original_codes: {original_codes[:50]}...")

            except json.JSONDecodeError:
                prompt = "Invalid JSON"
                language = "unknown"
                print("Received data is not valid JSON. Using default prompt.")

            # 模拟生成代码和处理时间
            if type == 'generate':
                mock_code = generate_mock_code_generate(prompt, language)
            elif type == 'edit':
                mock_code = generate_mock_code_edit(prompt, language, original_codes)
            
            # 模拟服务器处理延迟
            time.sleep(random.uniform(0.01, 0.1)) 

            # 准备 JSON 格式的响应
            response_json = {
                "status": "success",
                "code": mock_code,
                "message": f"Successfully generated mock code for prompt: {prompt[:20]}..."
            }
            
            response = json.dumps(response_json).encode('utf-8')
            
            # 发送响应回客户端
            self.request.sendall(response)
            self.finish()
            print("  Response sent to client.")
            
        except Exception as e:
            print(f"An error occurred during handling: {e}")

# ----------------------------------------------------
# 启动 Server
# ----------------------------------------------------
if __name__ == "__main__":
    try:
        # 使用 ThreadingMixIn 确保服务器可以同时处理多个请求 (多线程)
        server = socketserver.ThreadingTCPServer((HOST, PORT), AIServerHandler)
        print("="*50)
        print(f"🚀 Starting Debug AI Server on {HOST}:{PORT}")
        print("Press Ctrl+C to stop.")
        print("="*50)
        
        # 保持服务器运行
        server.serve_forever()

    except KeyboardInterrupt:
        print("\nShutting down server...")
    except Exception as e:
        print(f"Failed to start server: {e}")
    finally:
        if 'server' in locals():
            server.server_close()
            print("Server closed.")