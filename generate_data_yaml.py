import yaml
import os

# === Đường dẫn tuyệt đối đến các file lớp ===
base_dir = r"D:\smartTrafficWithYOLO\HeThongGiaoThongThongMinh\Data_mẫu\archive"
en_file = os.path.join(base_dir, "classes_en.txt")
vie_file = os.path.join(base_dir, "classes_vie.txt")
code_file = os.path.join(base_dir, "classes.txt")  # có thể dùng nếu cần mã số class sau này

# === Kiểm tra sự tồn tại của file ===
for path in [en_file, vie_file]:
    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ Không tìm thấy file: {path}")

# === Đọc file lớp ===
with open(en_file, "r", encoding="utf-8") as f_en, \
     open(vie_file, "r", encoding="utf-8") as f_vie:
    en_names = [line.strip() for line in f_en if line.strip()]
    vie_names = [line.strip() for line in f_vie if line.strip()]

# === Kiểm tra độ dài 2 file khớp nhau ===
if len(en_names) != len(vie_names):
    raise ValueError(f"⚠️ Số dòng không khớp giữa classes_en.txt ({len(en_names)}) và classes_vie.txt ({len(vie_names)})")

# === Kết hợp song ngữ ===
names = [f"{en} - {vie}" for en, vie in zip(en_names, vie_names)]

# === Tạo cấu trúc YAML ===
data = {
    "train": r"d:/smartTrafficWithYOLO/datasets/train/images",
    "val": r"d:/smartTrafficWithYOLO/datasets/val/images",
    "test": r"d:/smartTrafficWithYOLO/datasets/test/images",
    "nc": len(names),
    "names": names
}

# === Ghi ra file data.yaml ===
with open("data.yaml", "w", encoding="utf-8") as f:
    yaml.dump(data, f, allow_unicode=True, sort_keys=False)

print(f"✅ File data.yaml đã được tạo thành công với {len(names)} lớp (song ngữ Anh - Việt).")
