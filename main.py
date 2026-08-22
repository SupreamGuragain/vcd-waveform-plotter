import sys
import os
from waveform_engine import convert_vcd_to_png

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_vcd_file> [output_image_path]")
        sys.exit(1)

    vcd_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "waveform.png"

    if not os.path.exists(vcd_file):
        print(f"Error: File '{vcd_file}' not found.")
        sys.exit(1)

    convert_vcd_to_png(vcd_file, output_file)