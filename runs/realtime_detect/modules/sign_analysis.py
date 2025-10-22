def analyze_sign(class_id):
    """
    Phân tích biển báo dựa trên class_id.
    Trả về thông tin dạng dict để hiển thị hoặc cảnh báo.
    """
    sign_dict = {
        0: {"name": "Dừng lại", "type": "Cấm", "advice": "Giảm tốc độ và dừng trước vạch."},
        1: {"name": "Rẽ trái", "type": "Chỉ dẫn", "advice": "Được phép rẽ trái khi an toàn."},
        2: {"name": "Rẽ phải", "type": "Chỉ dẫn", "advice": "Được phép rẽ phải khi an toàn."},
        3: {"name": "Cấm rẽ phải", "type": "Cấm", "advice": "Không rẽ phải tại khu vực này."},
        4: {"name": "Tốc độ tối đa 50km/h", "type": "Giới hạn tốc độ", "advice": "Giữ tốc độ ≤ 50km/h."},
    }

    return sign_dict.get(class_id, {"name": f"Biển báo #{class_id}", "type": "Khác", "advice": "Quan sát kỹ và tuân thủ."})
