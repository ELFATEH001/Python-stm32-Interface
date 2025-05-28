import serial
from datetime import datetime

COM_PORT = 'COM6'
BAUD_RATE = 9600  # Must match STM32 UART settings

try:
    with serial.Serial(COM_PORT, BAUD_RATE, timeout=1) as ser:
        print(f"Listening on {COM_PORT} at {BAUD_RATE} baud...\nPress Ctrl+C to exit.")
        while True:
            data = ser.read(32)  # Read up to 32 bytes (max expected length)
            if data:
                timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
                message = data.decode(errors='ignore').strip()
                print(f"[{timestamp}] Received: {message}")
except serial.SerialException as e:
    print("Serial error:", e)
except KeyboardInterrupt:
    print("\nStopped by user.")