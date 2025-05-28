import serial
from datetime import datetime

COM_PORT = 'COM6'
BAUD_RATE = 9600  # Must match STM32 UART settings

def parse_csv_line(line):
    if line.startswith("DATA:"):
        try:
            parts = line[5:].strip().split(',')
            if len(parts) >= 3:
                values = [float(v)/1000 for v in parts[:3]]
                return values
        except ValueError:
            pass
    return None

try:
    with serial.Serial(COM_PORT, BAUD_RATE, timeout=1) as ser:
        print(f"Listening on {COM_PORT} at {BAUD_RATE} baud...\nPress Ctrl+C to exit.")
        while True:
            data = ser.read(200)  # Read up to 64 bytes
            if data:
                timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
                message = data.decode(errors='ignore').strip()
                print(f"[{timestamp}] Raw: {message}")
except serial.SerialException as e:
    print("Serial error:", e)
except KeyboardInterrupt:
    print("\nStopped by user.")
