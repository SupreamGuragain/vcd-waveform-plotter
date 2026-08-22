# VCD Waveform Plotter

A lightweight Python utility designed to parse Verilog Value Change Dump (`.vcd`) simulation files and render high-resolution waveform images automatically.

## Features
- **Dark-Theme Visuals:** Renders digital signals using `matplotlib` with a modern dark theme.
- **Multi-Bit Bus Decoding:** Automatically detects multi-bit vectors (e.g., `data[7:0]`) and formats state changes into hexadecimal labels.
- **Headless & Fast:** Generates visual graphs without launching bulky GUI software like GTKWave.
- **Agent Integration:** Easy to import into automated AI chip design pipelines.

## Installation
```bash
pip install -r requirements.txt