import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from distance_estimation import estimate_distance
from sign_analysis import analyze_sign
from log_manager import log_event, alert_user

from ultralytics import YOLO
import cv2



model = YOLO("D:\\smartTrafficWithYOLO\\runs\\detect\\train3\\weights\\best.pt")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Không thể mở webcam.")
    exit()

print("✅ Hệ thống nhận dạng biển báo giao thông đang khởi động...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # === Nhận dạng biển báo ===
    results = model.predict(source=frame, stream=True, conf=0.25)

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # === Ước lượng khoảng cách ===
            distance = estimate_distance(x1, y1, x2, y2)

            # === Phân tích biển báo ===
            info = analyze_sign(cls)
            name = info["name"]
            advice = info["advice"]

            # === Cảnh báo & log ===
            alert_msg = f"{name} ({distance}m) - {advice}"
            alert_user(alert_msg)
            log_event(f"{name}, distance={distance}m, conf={conf:.2f}")

            # === Vẽ bounding box ===
            color = (0, 255, 0) if info["type"] != "Cấm" else (0, 0, 255)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{name} {distance}m", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    cv2.imshow("Smart Traffic System (Realtime)", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        print("🛑 Đang tắt hệ thống...")
        break

cap.release()
cv2.destroyAllWindows()
print("✅ Đã dừng hệ thống.")
