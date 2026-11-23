# -*- coding: utf-8 -*-
"""
run_all_validations.py — Master One-Command Mathematical Validation &
Publication Figure Generator for The Conciseness Framework (Pillars 1–5).

Executes:
  1. Generates root architectural DAG schematic (`figures/fig0_framework_architecture_dag.png/.svg`).
  2. Executes standalone proof & numerical verification scripts for Pillars 1–5:
     - 01_Foundation_of_Knowledge/validate_pillar1_foundation.py
     - 02_Finite_Infinity_Framework/validate_pillar2_finite_infinity.py
     - 03_Actualization_Theory/validate_pillar3_actualization.py
     - 04_Computational_Knowledge_Theory/validate_pillar4_ckt.py
     - 05_Consciousness_Prime_Reductions/validate_pillar5_consciousness.py
"""

import subprocess
import sys
import time
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

NAVY = "#0A1C3F"
TEAL = "#1B7F79"
BLUE = "#1E40AF"
SLATE = "#475569"
LIGHT_BG = "#F8FAFC"
MUTED_BG = "#F1F5F9"


def generate_architecture_diagram():
    """Render publication-grade architectural DAG for The Conciseness Framework (Pillars 1–5)."""
    plt.rcParams.update({
        "font.family": "DejaVu Serif",
        "figure.facecolor": "white",
        "savefig.dpi": 300,
    })

    fig, ax = plt.subplots(figsize=(11.5, 8.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10.6)
    ax.axis("off")

    ax.text(
        5.0, 10.22,
        "THE CONCISENESS FRAMEWORK — DEDUCTIVELY CLOSED ARCHITECTURE (PILLARS 1–5)",
        ha="center", va="center", fontsize=12.0, fontweight="bold", color=NAVY,
    )
    ax.text(
        5.0, 9.86,
        "Strict Directed Acyclic Hierarchy · Zero Forward References · Unified Five-Prime Basis",
        ha="center", va="center", fontsize=9.2, style="italic", color=SLATE,
    )

    nodes = [
        {
            "y": 8.40, "h": 1.15, "fc": "#EEF2FF", "ec": NAVY,
            "title": "PILLAR 1 — The Foundation of Knowledge Theory (v2.10)",
            "body": (
                "Immutable Ontological & Epistemological Root: Performative Understanding (Phi), Nothingness Impossibility,\n"
                "Event vs. Non-Event Exemption (Box E_A), Five Conceptual Primes P_C = {O, K, P, J, M}, Mercy–Time Bridge, Triad of Balance"
            ),
        },
        {
            "y": 6.80, "h": 1.15, "fc": "#ECFDF5", "ec": TEAL,
            "title": "PILLAR 2 — The Finite Infinity Framework (v2.0)",
            "body": (
                "1+3 Domain Architecture (Dom_R vs. Dom_P, Dom_M, Dom_C), Non-Compensatory Compliance P_hat_D(R),\n"
                "Operational Floor (delta_act, dt_min > 0), Ontological Curvature (B_cost, ||dX||_crit), Beginning Finitude & 8 Paradoxes"
            ),
        },
        {
            "y": 5.20, "h": 1.15, "fc": "#EFF6FF", "ec": BLUE,
            "title": "PILLAR 3 — The Actualization Theory (v6.0)",
            "body": (
                "Universal Dynamical Selection Engine: Banach Contraction T_M (k_D), Atomic Lattice B_fin, 5D Prime Orthant H_P^+,\n"
                "Domain Drift Hessian D_uv^(D), Dual Bifurcation, Stationary Drift W_caus, Fractal Transfer (R_l, phi), Simplex w* & Saturation v_inf"
            ),
        },
        {
            "y": 3.60, "h": 1.15, "fc": "#F0FDFA", "ec": "#0F766E",
            "title": "PILLAR 4 — The Computational Knowledge Theory (v4.0)",
            "body": (
                "Information-Complexity & Unsimulable Reality: Log-Barrier v_i = -ln P_i, Mean-Normalized C_inf (Prop 1.1),\n"
                "Debreu–Aczel Uniqueness, Contractive CAKI = 1 - k_eff < 1, Landauer P_wisdom [bits/s], Dual Unsimulability & Ascending Helix"
            ),
        },
        {
            "y": 1.95, "h": 1.20, "fc": "#FEF3C7", "ec": "#B45309",
            "title": "PILLAR 5 — Consciousness Operations as Prime Reductions (v4.0 · Cognition Domain)",
            "body": (
                "Embodied Cognition & Knowledge-Density Acceleration: Qualia Termination Psi_Q, Intelligence Emergence & Bounded Sandboxes,\n"
                "11 Non-Commuting Question Operators Q_omega (alpha_omega), Subjective Prime E_hat, Multi-Horizon W_caus, CoEx (W_e >= W_p), Thm 8.1"
            ),
        },
    ]

    for idx, nd in enumerate(nodes):
        box = FancyBboxPatch(
            (0.65, nd["y"]), 8.70, nd["h"],
            boxstyle="round,pad=0.06,rounding_size=0.14",
            facecolor=nd["fc"], edgecolor=nd["ec"], linewidth=1.8,
        )
        ax.add_patch(box)
        ax.text(
            5.0, nd["y"] + nd["h"] * 0.72, nd["title"],
            ha="center", va="center", fontsize=9.8, fontweight="bold", color=NAVY,
        )
        ax.text(
            5.0, nd["y"] + nd["h"] * 0.31, nd["body"],
            ha="center", va="center", fontsize=8.0, color="#1E293B", linespacing=1.35,
        )
        if idx < len(nodes) - 1:
            y_top = nd["y"]
            y_bot = nodes[idx + 1]["y"] + nodes[idx + 1]["h"] + 0.06
            ax.annotate(
                "", xy=(5.0, y_bot), xytext=(5.0, y_top - 0.04),
                arrowprops=dict(arrowstyle="-|>,head_width=0.28,head_length=0.4", color=NAVY, lw=1.8),
            )

    # Downstream forthcoming notice box (minimal, zero premature details)
    forth = FancyBboxPatch(
        (1.60, 0.35), 6.80, 0.85,
        boxstyle="round,pad=0.05,rounding_size=0.12",
        facecolor=MUTED_BG, edgecolor=SLATE, linewidth=1.2, linestyle="--",
    )
    ax.add_patch(forth)
    ax.text(
        5.0, 0.77,
        "Forthcoming Series Extensions (In Preparation — Zero Premature Forward References):\n"
        "Pillar 6 (The First Quanta Theory)  &  Pillar 7 (Prime-Base Intelligence)",
        ha="center", va="center", fontsize=8.2, color=SLATE, linespacing=1.35, style="italic",
    )
    ax.annotate(
        "", xy=(5.0, 1.26), xytext=(5.0, 1.89),
        arrowprops=dict(arrowstyle="-|>,head_width=0.22,head_length=0.35", color=SLATE, lw=1.3, ls="--"),
    )

    fig.tight_layout()
    for ext in ("png", "svg"):
        fig.savefig(FIG_DIR / f"fig0_framework_architecture_dag.{ext}", bbox_inches="tight")
    plt.close(fig)
    print(f"[PASS] Architectural DAG generated -> {FIG_DIR / 'fig0_framework_architecture_dag.png'}")


def main():
    t0 = time.perf_counter()
    print("================================================================================")
    print("  THE CONCISENESS FRAMEWORK — FULL MATHEMATICAL VALIDATION SUITE (PILLARS 1–5)  ")
    print("================================================================================\n")

    generate_architecture_diagram()
    print()

    scripts = [
        ROOT / "01_Foundation_of_Knowledge" / "validate_pillar1_foundation.py",
        ROOT / "02_Finite_Infinity_Framework" / "validate_pillar2_finite_infinity.py",
        ROOT / "03_Actualization_Theory" / "validate_pillar3_actualization.py",
        ROOT / "04_Computational_Knowledge_Theory" / "validate_pillar4_ckt.py",
        ROOT / "05_Consciousness_Prime_Reductions" / "validate_pillar5_consciousness.py",
    ]

    for script in scripts:
        if not script.exists():
            raise FileNotFoundError(f"Missing validation script: {script}")
        res = subprocess.run([sys.executable, str(script)], text=True)
        if res.returncode != 0:
            raise RuntimeError(f"Validation script failed with exit code {res.returncode}: {script}")
        print()

    elapsed = time.perf_counter() - t0
    print("================================================================================")
    print(f"  ALL PILLARS (1–5) MATHEMATICAL PROOFS & FIGURES VERIFIED IN {elapsed:.2f}s  ")
    print("================================================================================")


if __name__ == "__main__":
    main()
