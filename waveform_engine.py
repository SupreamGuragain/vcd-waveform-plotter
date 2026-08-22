import matplotlib.pyplot as plt
from vcdvcd import VCDVCD

def convert_vcd_to_png(vcd_path, output_path="output.png"):
    vcd = VCDVCD(vcd_path)
    signals = list(vcd.signals)
    
    plt.style.use("dark_background")
    fig, axes = plt.subplots(len(signals), 1, figsize=(10, 2 * len(signals)), sharex=True)
    if len(signals) == 1:
        axes = [axes]

    for ax, sig in zip(axes, signals):
        tv = vcd[sig].tv  # List of (time, value) tuples
        times = [t for t, v in tv]
        vals = [v for t, v in tv]

        # Check if vector/multi-bit bus (e.g. 'b1010' or length > 1)
        is_bus = any(isinstance(v, str) and (v.startswith('b') or len(v) > 1) for v in vals)

        if not is_bus:
            # Single-bit digital trace
            int_vals = [int(v) if v in ['0', '1'] else 0 for v in vals]
            ax.step(times, int_vals, where='post', color='#00FFCC', linewidth=2)
            ax.set_ylim(-0.2, 1.2)
            ax.set_yticks([0, 1])
        else:
            # Multi-bit bus rendering
            ax.set_ylim(-0.2, 1.2)
            ax.axhline(0, color='#FF8C00', linestyle='--', alpha=0.5)
            ax.axhline(1, color='#FF8C00', linestyle='--', alpha=0.5)
            ax.set_yticks([])
            
            for i in range(len(times) - 1):
                t_start, t_end = times[i], times[i + 1]
                val = vals[i]
                # Convert binary string to Hex label
                try:
                    clean_val = val.lstrip('b')
                    hex_str = f"0x{int(clean_val, 2):X}"
                except ValueError:
                    hex_str = str(val)

                ax.text((t_start + t_end) / 2, 0.5, hex_str, 
                        ha='center', va='center', color='#FF8C00', fontsize=9, fontweight='bold')

        ax.set_ylabel(sig.split('.')[-1], rotation=0, labelpad=25, color='white', fontweight='bold')
        ax.grid(True, linestyle=':', alpha=0.3)

    plt.xlabel("Time (ps)", color='white')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

if __name__ == "__main__":
    import sys
    convert_vcd_to_png(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "output.png")