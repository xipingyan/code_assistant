import socket
import json
import sys
from datetime import datetime

# ----------------------------------------------------
# 连接配置 (需与 Server 配置保持一致)
# ----------------------------------------------------
HOST = "127.0.0.1"
PORT = 8080

def test_server_connection(prompt_text: str, request_type: str = "generate", language: str = "python"):
    """
    连接到本地服务器，发送一个请求，并打印响应。
    
    参数:
    - prompt_text: 发送给 AI 的指令。
    - request_type: 'generate' (光标位置生成) 或 'context_aware' (选中代码处理)。
    - language: 当前文件的编程语言。
    """
    
    # 构造请求数据 (模拟插件发送的 JSON)
    request_data = {
        "type": request_type,
        "prompt": prompt_text,
        "language": language,
        "context_code": f"// This is placeholder code context for a {language} file." if request_type == "context_aware" else None
    }
    
    # 将字典转换为 JSON 字符串
    message = json.dumps(request_data).encode('utf-8')
    
    print("="*60)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Attempting to connect to {HOST}:{PORT}")

    try:
        # 创建一个 TCP/IP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            # 连接到服务器
            client_socket.connect((HOST, PORT))
            print("✅ Successfully connected to the server.")
            
            # 发送数据
            client_socket.sendall(message)
            print(f"➡️ Sent {len(message)} bytes. Request type: '{request_type}'")
            print(f"   Prompt: '{prompt_text}'")

            client_socket.shutdown(socket.SHUT_WR)

            # 接收响应
            response_chunks = []
            while True:
                # 接收 1024 字节的数据块
                chunk = client_socket.recv(1024)
                if not chunk:
                    break
                response_chunks.append(chunk)

            full_response = b"".join(response_chunks).decode('utf-8')
            
            if not full_response:
                print("❌ Received empty response from server.")
                return

            print("\n" + "~"*20 + " SERVER RESPONSE " + "~"*20)
            
            # 尝试解析 JSON 响应
            try:
                response_json = json.loads(full_response)
                
                print("Response JSON Status:", response_json.get('status', 'N/A'))
                print("Response Message:", response_json.get('message', 'N/A'))
                print("\n--- GENERATED CODE ---\n")
                print(response_json.get('code', 'Code field missing.'))
                print("\n----------------------")
                
            except json.JSONDecodeError:
                print("❌ Error: Received data is not valid JSON.")
                print("Raw Response:\n", full_response)
                
    except ConnectionRefusedError:
        print(f"❌ Connection Refused: Ensure the server is running on {HOST}:{PORT}.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ An error occurred: {e}")
    finally:
        print("="*60)

if __name__ == "__main__":
    # --- 测试用例 1: 简单代码生成 ---
    test_server_connection(
        prompt_text="Write a function to calculate Fibonacci sequence.",
        request_type="generate",
        language="python"
    )

    # --- 测试用例 2: 上下文处理 (模拟选中代码) ---
    test_server_connection(
        prompt_text="Optimize the selected code for performance.",
        request_type="context_aware",
        language="typescript"
    )