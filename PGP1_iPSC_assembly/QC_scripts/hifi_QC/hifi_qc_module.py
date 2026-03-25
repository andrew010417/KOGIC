#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import pysam
import matplotlib.pyplot as plt
import argparse

# ----------------------------
# NanoPlot QC
# ----------------------------
def run_nanoplot(fastq_file, outdir, threads=8):
    """NanoPlot QC 실행"""
    os.makedirs(outdir, exist_ok=True)
    cmd = [
        "NanoPlot",
        "--fastq", fastq_file,
        "--threads", str(threads),
        "--outdir", outdir
    ]
    print(f"[NanoPlot] Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)
    print(f"[NanoPlot] Done! Results in {outdir}")

# ----------------------------
# RQ QC
# ----------------------------
def check_rq(bam_file, out_file, hist_file):
    """BAM에서 RQ 통계 계산 및 히스토그램 저장"""
    total = 0
    good = 0
    rq_list = []

    with pysam.AlignmentFile(bam_file, "rb") as bam:
        for read in bam:
            if read.has_tag("rq"):
                rq = read.get_tag("rq")
                rq_list.append(rq)
                total += 1
                if rq >= 0.99:
                    good += 1

    fraction = good / total if total > 0 else 0
    mean_rq = sum(rq_list) / total if total > 0 else 0
    min_rq = min(rq_list) if rq_list else 0
    max_rq = max(rq_list) if rq_list else 0

    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    os.makedirs(os.path.dirname(hist_file), exist_ok=True)

    with open(out_file, "w") as f:
        f.write(f"total RQ tags = {total}\n")
        f.write(f"good RQ tags (>=0.99) = {good}\n")
        f.write(f"fraction = {fraction:.4f}\n")
        f.write(f"mean RQ = {mean_rq:.4f}\n")
        f.write(f"min RQ = {min_rq:.4f}\n")
        f.write(f"max RQ = {max_rq:.4f}\n")

    print(f"[RQ QC] Done! Results saved to {out_file}")

    plt.figure(figsize=(8,5))
    plt.hist(rq_list, bins=50, color='skyblue', edgecolor='black')
    plt.title('HiFi Read RQ Distribution')
    plt.xlabel('RQ')
    plt.ylabel('Read count')
    plt.savefig(hist_file, dpi=150)
    plt.close()
    print(f"[RQ QC] Histogram saved to {hist_file}")

# ----------------------------
# 독립 실행용
# ----------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HiFi QC module standalone run")
    parser.add_argument("--fastq", help="Input FASTQ for NanoPlot")
    parser.add_argument("--bam", help="Input BAM for RQ check")
    parser.add_argument("--outdir", required=True, help="Output directory")
    parser.add_argument("-t", "--threads", type=int, default=8, help="Threads for NanoPlot")
    args = parser.parse_args()

    if args.fastq:
        nanoplot_out = os.path.join(args.outdir, "NanoPlot")
        run_nanoplot(args.fastq, nanoplot_out, args.threads)

    if args.bam:
        rq_txt = os.path.join(args.outdir, "RQ_results.txt")
        rq_hist = os.path.join(args.outdir, "RQ_histogram.png")
        check_rq(args.bam, rq_txt, rq_hist)