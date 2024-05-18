import requests
from tqdm import tqdm
import os
import subprocess
# 设置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11"
}
npm = 0
ollama = 0
git = 0
# 创建下载文件夹
print("下载自检")
filepath = "c:/ollamarunner/"
if os.path.exists("c:/ollamarunner/"):
    print("下载环境自检完成")
else:
    os.makedirs(filepath, exist_ok=True)
    print("下载环境有误，依赖已补齐")

print("ollama runner自检中......")
ollama_try = requests.get("https://ollama.com", headers=headers,  verify=False)

print("网络自检")
print("正在连接到ollama服务器", ollama_try.status_code)
if ollama_try.status_code == 200:
    print("连接成功 200 OK")
    print("网络自检成功")
else:
    print("ERROR: 连接失败")
    exit()

print("自检结束，欢迎使用ollama runner")

url = 'https://kkgithub.com/ollama/ollama/releases/download/v0.1.38/OllamaSetup.exe'
filename = 'ollama.exe'
urlnodejs = 'https://nodejs.org/dist/v18.12.1/node-v18.12.1-x64.msi'
filenamenodejs = "nodejs.msi"
urlgit = 'https://kkgithub.com/git-for-windows/git/releases/download/v2.45.1.windows.1/Git-2.45.1-64-bit.exe'
filenamegit = 'git.exe'
def download_file(url, filename):
    if not os.path.exists(os.path.join(filepath, filename)):
        response = requests.get(url, stream=True, headers=headers, verify=False)
        total_size = int(response.headers.get('Content-Length', 0))

        with open(os.path.join(filepath, filename), 'wb') as file:
            with tqdm(total=total_size, unit='iB', unit_scale=True) as progress_bar:
                for data in response.iter_content(chunk_size=8192):
                    file.write(data)
                    progress_bar.update(len(data))
    else:
        print(f"文件 {filename} 已存在")

def download_nodejs(urlnodejs, filenamenodejs):
    if not os.path.exists(os.path.join(filepath, filenamenodejs)):
        response = requests.get(urlnodejs, stream=True, headers=headers, verify=False)
        total_size = int(response.headers.get('Content-Length', 0))

        with open(os.path.join(filepath, filenamenodejs), 'wb') as file:
            with tqdm(total=total_size, unit='iB', unit_scale=True) as progress_bar:
                for data in response.iter_content(chunk_size=8192):
                    file.write(data)
                    progress_bar.update(len(data))
    else:
        print(f"文件 {filenamenodejs} 已存在")
def download_git(urlgit, filenamegit):
    if not os.path.exists(os.path.join(filepath, filenamegit)):
        response = requests.get(urlgit, stream=True, headers=headers, verify=False)
        total_size = int(response.headers.get('Content-Length', 0))

        with open(os.path.join(filepath, filenamegit), 'wb') as file:
            with tqdm(total=total_size, unit='iB', unit_scale=True) as progress_bar:
                for data in response.iter_content(chunk_size=8192):
                    file.write(data)
                    progress_bar.update(len(data))
    else:
        print(f"文件 {filenamegit} 已存在")
def check_installation(command):
    #result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
    result = os.system(command)
    result = str(result)
    if '不是内部或外部命令，也不是可运行的程序或批处理文件。' in result:
        print("未安装",command)
        return f"{command} 未安装"
    else:
        print(command ,"已安装")
        return f"{command} 已安装"
def check_end():
    global npm , ollama ,git
    checknpm = check_installation("npm")
    print(checknpm)
    if '已安装' in checknpm:
        npm = 1
    checkollama = check_installation("ollama")
    print(checkollama)
    if '已安装' in checkollama:
        ollama = 1
    checkgit = check_installation("git")
    if '已安装' in checkgit:
        git = 1
def run_ai():
    check_end()
    if git == 1 and ollama == 1 and npm == 1:
        print("自检通过，以下模型可以运行")
        print('|模型名称             |训练参数    |大小   |')
        print('| llama3             | 8B         | 4.7GB |')
        print('| llama3:70b         | 70B        | 40GB  |')
        print('| phi3               | 3.8B       | 2.3GB |')
        print('| mistral            | 7B         | 4.1GB |')
        print('| neural-chat        | 7B         | 4.1GB |')
        print('| starling-lm        | 7B         | 4.1GB |')
        print('| codellama          | 7B         | 3.8GB |')
        print('| llama2-uncensored  | 7B         | 3.8GB |')
        print('| llava              | 7B         | 4.5GB |')
        print('| gemma:2b           | 2B         | 1.4GB |')
        print('| gemma:7b           | 7B         | 4.8GB |')
        print('| codegemma:7b       | 7B         | 4.8GB |')
        print('| codegemma:2b       | 2B         | 1.4GB |')
        print("| solar              | 10.7B      | 6.1GB |")
        html = input("是否启用前端[y/n]")
        if html == 'y':
            github = requests.get("https://www.github.com", headers=headers,verify=False)
            print("正在连接到github服务器", github.status_code)
            if github.status_code == 200:
                print("连接成功 200 OK")
                print("网络自检成功")
                os.system("git clone https://githubfast.com/jakobhoeg/nextjs-ollama-llm-ui c:/ollamarunner/ ; cd c:/ollamarunner/nextjs-ollama-llm-ui ; move .example.env .env ; npm install ; npm run dev")
                ai_data = input("请输入要运行的模型名称（见上表）")
                os.system("ollama run " + ai_data)
                print('已结束')
            else:
                print("ERROR: 连接失败")
            exit()
        else:
            ai_data = input("请输入要运行的模型名称（见上表）")
        #subprocess.run('ollama run' + ai_data, shell=True, capture_output=True, text=True)
            os.system("ollama run " + ai_data)
            print('对话结束')
    else:
        print("请下载ollama,git,nodejs")
def about():
    print("关于ollama runner")
    print("作者：张涵哲")
    print("作者博客：https://zhanghanzhe666.github.io/")
def start_ui():
    print("欢迎使用ollama runner")
    print("[1]下载并安装ollama")
    print("[2]运行模型")
    print("[3]关于")
    print('[4]下载nodejs(聊天前端服务器支持)')
    print('[5]下载git')
    print("请输入数字选择")
    que = input()
    que = int(que)
    if que == 1:
        download_file(url, filename)
        subprocess.call('cd C:/ollamarunner & ollama.exe', shell=True)
        print("ollama安装程序已开始运行")
    elif que == 2:
        run_ai() 
    elif que == 3:
        about()
    elif que == 4:
        download_nodejs(urlnodejs, filenamenodejs)
        subprocess.call('cd C:/ollamarunner & nodejs.msi', shell=True)
        print("nodejs安装程序已开始运行")
    elif que == 5:
        download_git(urlgit, filenamegit)
        subprocess.call('cd C:/ollamarunner & git.exe', shell=True)
        print("git安装程序已开始运行")
    elif que == 124658:
        #开发者选项
        check_end()

    else:
        print("请输入有效的选项")

while True:
    start_ui()
