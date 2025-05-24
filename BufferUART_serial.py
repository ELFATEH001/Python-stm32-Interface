import serial

# Replace with your actual COM port (e.g., COM3 on Windows, /dev/ttyUSB0 on Linux)
COM_PORT = 'COM6'
BAUD_RATE = 9600  # Make sure it matches the STM32 configuration

try:
    with serial.Serial(COM_PORT, BAUD_RATE, timeout=1) as ser:
        print(f"Listening on {COM_PORT} at {BAUD_RATE} baud...\nPress Ctrl+C to exit.")
        while True:
            data = ser.read(10)  # Wait to receive exactly 10 bytes
            if len(data) == 10:
                # Print the raw byte values
                print("Received:", list(data))
except serial.SerialException as e:
    print("Serial error:", e)
except KeyboardInterrupt:
    print("\nStopped by user.")
