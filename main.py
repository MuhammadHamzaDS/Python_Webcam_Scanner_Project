import cv2
import mysql.connector

# ✅ MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="lenovo&9090",
    database="barcode_system"
)
cursor = conn.cursor()

def insert_to_db(data):
    query = "INSERT INTO scanned_items (barcode_data) VALUES (%s)"
    cursor.execute(query, (data,))
    conn.commit()
    print(f"✅ Data inserted: {data}")

# ✅ QR Scanner Initialization
cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
scanned = set()

print("📸 Webcam started... Show QR code in front of camera (Press 'q' to quit)")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect and decode QR
    data, bbox, _ = detector.detectAndDecode(frame)
    if data:
        if data not in scanned:
            insert_to_db(data)
            scanned.add(data)

        # Draw bounding box
        if bbox is not None:
            bbox = bbox.astype(int)
            for i in range(len(bbox[0])):
                cv2.line(frame, tuple(bbox[0][i]), tuple(bbox[0][(i+1) % len(bbox[0])]), (0, 255, 0), 2)
            cv2.putText(frame, "Scanned!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("QR Scanner", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
conn.close()
print("👋 Scanner closed successfully.")
