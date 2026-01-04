import os

label_dir = r"labels"  

found = False

for root, _, files in os.walk(label_dir):
    for name in files:
        if not name.endswith(".txt"):
            continue

        path = os.path.join(root, name)
        with open(path, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue

                parts = line.split()
                cls = int(parts[0])

                if cls == 4:
                    print(f"发现标签 4 → 文件: {path}, 行号: {line_num}")
                    found = True

if not found:
    print("未发现任何类别为 4 的标签")
