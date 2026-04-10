import os
import sys
import requests
import time
import random

def log(msg):
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def main():
    user_id = os.getenv('NETEASE_USER_ID')
    cookie = os.getenv('NETEASE_COOKIE')
    if not user_id or not cookie:
        log("❌ 错误：未找到必要的 Secrets 配置 (NETEASE_USER_ID 或 NETEASE_COOKIE)")
        sys.exit(1)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Cookie': cookie
    }
    try:
        # 1. 签到逻辑
        log("正在尝试签到...")
        sign_url = f"https://music.163.com/api/signin?userId={user_id}"
        res = requests.get(sign_url, headers=headers, timeout=15)
        if res.status_code == 200:
            log(f"签到请求成功: {res.text}")
        else:
            log(f"签到请求失败，状态码: {res.status_code}")
            sys.exit(1)

        # 2. 模拟听歌刷级逻辑
        log("开始模拟听歌刷级...")
        test_ids = ["123456", "789012", "345678"]
        for song_id in test_ids:
            play_url = f"https://music.163.com/api/song/play?id={song_id}"
            wait_time = random.randint(5, 15)
            log(f"模拟播放歌曲 {song_id}，等待 {wait_time} 秒...")
            requests.get(play_url, headers=headers, timeout=15)
            time.sleep(wait_time)
        log("✅ 所有自动化任务执行完毕！")
    except Exception as e:
        log(f"❌ 运行过程中出现致命错误: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
