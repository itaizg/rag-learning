"""Run this script once to generate the synthetic Helios images."""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
import numpy as np
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).parent

# ── 1. HeliosArm V2 joint diagram ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(6, 8), facecolor="#f0f4f8")
ax.set_xlim(-2, 2); ax.set_ylim(-1, 7); ax.axis("off")
ax.set_title("HeliosArm V2 — Joint Diagram (HR-ARM-V2-6DOF)", fontsize=11, fontweight="bold")

# Draw simplified stick arm
joints = [(0, 0), (0, 1), (0.5, 2.5), (0.8, 4), (0.6, 5.2), (0.4, 6.2)]
labels = ["J1 Base\n±170°", "J2 Shoulder\n±130°", "J3 Elbow\n±150°",
          "J4 Wrist Roll\n±180°", "J5 Wrist Pitch\n±120°", "J6 Wrist Yaw\n±360°"]
colors = ["#2b5797", "#2b5797", "#2b5797", "#c0392b", "#2b5797", "#2b5797"]

for i, (x, y) in enumerate(joints):
    ax.plot(x, y, "o", markersize=14, color=colors[i], zorder=5)
    ax.annotate(labels[i], (x, y), xytext=(x + 0.25, y),
                fontsize=7.5, va="center", color="#333")

for i in range(len(joints) - 1):
    x1, y1 = joints[i]; x2, y2 = joints[i + 1]
    ax.plot([x1, x2], [y1, y2], "k-", lw=3, zorder=3)

ax.annotate("⚠ J4: limit to 120°/s above 38°C\n(see advisory BULL-2024-007)",
            (0.8, 4), xytext=(1.2, 3.4),
            fontsize=8, color="#c0392b",
            arrowprops=dict(arrowstyle="->", color="#c0392b"))

# Payload label
ax.text(0.4, 6.6, "End-effector\n12 kg payload", ha="center", fontsize=8,
        bbox=dict(boxstyle="round,pad=0.3", fc="#e8f5e9", ec="#4caf50"))

plt.tight_layout()
fig.savefig(OUT / "spec_arm_v2_joint_diagram.png", dpi=120, bbox_inches="tight")
plt.close()
print("Generated: spec_arm_v2_joint_diagram.png")

# ── 2. HeliosBase M1 top-view layout ─────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 7), facecolor="#f0f4f8")
ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5); ax.axis("off")
ax.set_title("HeliosBase M1 — Top View Layout (HR-MOB-M1-AMR)", fontsize=11, fontweight="bold")

# Body
body = mpatches.FancyBboxPatch((-0.7, -0.6), 1.4, 1.2,
                                boxstyle="round,pad=0.05", fc="#c8d6e5", ec="#2b5797", lw=2)
ax.add_patch(body)
ax.text(0, 0, "HeliosBase M1\n700×600 mm", ha="center", va="center", fontsize=9, fontweight="bold")

# Wheels
for x, y, lbl in [(-0.75, 0.45, "FL"), (0.75, 0.45, "FR"), (-0.75, -0.45, "RL"), (0.75, -0.45, "RR")]:
    wh = mpatches.FancyBboxPatch((x - 0.12, y - 0.2), 0.24, 0.4,
                                  boxstyle="round,pad=0.02", fc="#555", ec="#222", lw=1.5)
    ax.add_patch(wh)
    ax.text(x, y, lbl, ha="center", va="center", fontsize=7, color="white", fontweight="bold")

# LIDAR
lidar = plt.Circle((0, 0.55), 0.12, fc="#e74c3c", ec="#c0392b", lw=1.5)
ax.add_patch(lidar)
ax.text(0, 0.55, "LIDAR", ha="center", va="center", fontsize=6.5, color="white")

# Safety zones
warning_zone = plt.Circle((0, 0), 1.25, fill=False, ec="#f39c12", lw=1.5, ls="--", alpha=0.7)
protect_zone = plt.Circle((0, 0), 0.8, fill=False, ec="#e74c3c", lw=1.5, ls="-", alpha=0.7)
ax.add_patch(warning_zone)
ax.add_patch(protect_zone)

ax.text(0, 1.28, "Warning 1.5 m", ha="center", fontsize=8, color="#f39c12")
ax.text(0, 0.83, "Protect 0.5 m", ha="center", fontsize=8, color="#e74c3c")

plt.tight_layout()
fig.savefig(OUT / "spec_mobile_base_topview.png", dpi=120, bbox_inches="tight")
plt.close()
print("Generated: spec_mobile_base_topview.png")

# ── 3. Battery charge cycle vs capacity chart ─────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 4), facecolor="#f0f4f8")
cycles = np.linspace(0, 800, 200)
capacity = 100 * np.exp(-0.00025 * cycles) - 0.003 * np.maximum(cycles - 450, 0)
capacity = np.clip(capacity, 60, 100)

ax.plot(cycles, capacity, color="#2b5797", lw=2.5, label="Actual capacity")
ax.axvline(450, color="#f39c12", ls="--", lw=1.5, label="Calibration alert threshold (450 cycles)")
ax.axvline(500, color="#e74c3c", ls="--", lw=1.5, label="INC-2024-019 region (>500 cycles)")
ax.axhline(100, color="#aaa", ls=":", lw=1)
ax.fill_betweenx([60, 100], 500, 800, alpha=0.07, color="#e74c3c")

ax.set_xlabel("Charge Cycles")
ax.set_ylabel("Capacity (% of rated)")
ax.set_title("HR-BAT-48V40 — Capacity Fade vs Charge Cycles", fontsize=11, fontweight="bold")
ax.legend(fontsize=8)
ax.set_xlim(0, 800); ax.set_ylim(60, 105)
ax.grid(alpha=0.3)
plt.tight_layout()
fig.savefig(OUT / "spec_battery_capacity_chart.png", dpi=120, bbox_inches="tight")
plt.close()
print("Generated: spec_battery_capacity_chart.png")

# ── 4. HC-400 front panel diagram ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 4), facecolor="#f0f4f8")
ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off")
ax.set_title("HC-400 Controller — Front Panel (HC400-CTRL)", fontsize=11, fontweight="bold")

# Controller body
panel = mpatches.FancyBboxPatch((0.5, 0.5), 9, 4,
                                 boxstyle="round,pad=0.1", fc="#d6dde6", ec="#2b5797", lw=2)
ax.add_patch(panel)

# Status LED
led = plt.Circle((1.2, 3.8), 0.15, fc="#27ae60", ec="#1a7a40")
ax.add_patch(led)
ax.text(1.2, 3.4, "Status\nLED", ha="center", fontsize=7)

# Ports
ports = [
    (2.5, 3.5, "EtherCAT\nMASTER"),
    (3.5, 3.5, "EtherCAT\nSLAVE"),
    (4.8, 3.5, "GbE\nPendant"),
    (6.0, 3.5, "GbE\nNetwork"),
    (7.2, 3.5, "USB ×4"),
    (8.4, 3.5, "E-STOP\n×2"),
]
for x, y, lbl in ports:
    rect = mpatches.FancyBboxPatch((x - 0.45, y - 0.3), 0.9, 0.6,
                                    boxstyle="round,pad=0.05", fc="#2b5797", ec="#1a3a6b")
    ax.add_patch(rect)
    ax.text(x, y, lbl, ha="center", va="center", fontsize=6, color="white")

ax.text(5, 1.8, "HeliosControl HC-400\nSIL 2 Certified | 4 kHz Servo Rate", ha="center",
        fontsize=10, fontweight="bold", color="#2b5797")

plt.tight_layout()
fig.savefig(OUT / "spec_controller_hc400_panel.png", dpi=120, bbox_inches="tight")
plt.close()
print("Generated: spec_controller_hc400_panel.png")

print("\nAll images generated in", OUT)
