import serial
from datetime import datetime

# Replace with your actual COM port (e.g., COM3 on Windows, /dev/ttyUSB0 on Linux)
COM_PORT = 'COM6'
BAUD_RATE = 9600  # Must match STM32 UART settings

try:
    with serial.Serial(COM_PORT, BAUD_RATE, timeout=1) as ser:
        print(f"Listening on {COM_PORT} at {BAUD_RATE} baud...\nPress Ctrl+C to exit.")
        while True:
            data = ser.read(10)  # Read 10 bytes
            if len(data) == 10:
                #timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # With milliseconds
                timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]  # With milliseconds
                print(f"[{timestamp}] Received: {list(data)}")
except serial.SerialException as e:
    print("Serial error:", e)
except KeyboardInterrupt:
    print("\nStopped by user.")
