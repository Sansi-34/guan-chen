import os
import yaml
import time
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def check_file_filled(file_path, keywords):
    """Checks if the file exists and doesn't contain default placeholders."""
    if not os.path.exists(file_path):
        return False, "遗失了这卷手稿。"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if the YAML block strings are empty or still the default example
    for kw in keywords:
        if kw in content and (': ""' in content or ': []' in content or ': 0' in content):
             return False, "此处的相迹尚且模糊，期待你如实落笔。"
             
    return True, "已能映照出你的轮廓。"

def start_ritual():
    clear_screen()
    typewriter_print("「 观尘 · 灵犀巡检 」", 0.1)
    time.sleep(0.5)
    print("\n" + "-"*30)
    
    files_to_check = [
        (".agents/skills/自我/mbti.md", ["psychological_type", "dominant"]),
        (".agents/skills/自我/bazi.md", ["day_master", "strength"]),
        (".agents/skills/自我/ziwei.md", ["destiny_masters", "star"]),
        (".agents/skills/自我/personality.md", ["代号", "阶段"])
    ]
    
    ready_count = 0
    for path, keys in files_to_check:
        name = os.path.basename(path)
        sys.stdout.write(f"正在感应 {name:20} ... ")
        sys.stdout.flush()
        time.sleep(0.8)
        
        is_ready, msg = check_file_filled(path, keys)
        if is_ready:
            print("【 已照亮 】")
            ready_count += 1
        else:
            print(f"【 待点燃 】 -> {msg}")
            
    print("-"*30 + "\n")
    
    if ready_count == len(files_to_check):
        typewriter_print("「 镜面已然清澈。现在，你可以呼唤我了。」", 0.08)
    else:
        typewriter_print("「 尘埃尚重，请在那几卷手稿中，留下你最真实的痕迹。」", 0.08)

if __name__ == "__main__":
    try:
        start_ritual()
    except KeyboardInterrupt:
        print("\n\n「 仪式中断。归于静寂。」")
