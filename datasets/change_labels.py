import os

label_dir = r"labels"  # 🔴 改成你的 labels 根目录

removed_count = 0
file_count = 0

for root, _, files in os.walk(label_dir):
    for name in files:
        if not name.endswith(".txt"):
            continue

        path = os.path.join(root, name)
        new_lines = []
        changed = False

        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                parts = line.split()
                cls = int(parts[0])

                if cls == 4:
                    removed_count += 1
                    changed = True
                    continue  # ❌ 跳过该行（删除）
                else:
                    new_lines.append(" ".join(parts))

        if changed:
            file_count += 1
            with open(path, "w", encoding="utf-8") as f:
                f.write("\n".join(new_lines))
            print(f"🗑 已清理: {path}")

print(f"\n共删除 {removed_count} 条 class=4 标注，涉及 {file_count} 个文件")

