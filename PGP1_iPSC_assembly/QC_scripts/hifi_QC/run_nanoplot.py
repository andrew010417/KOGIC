#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import subprocess
import os

def run_nanoplot(fastq_file, outdir, threads=8):
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run NanoPlot QC for HiFi FASTQ")
    parser.add_argument("-f", "--fastq", required=True, help="Input FASTQ file")
    parser.add_argument("-o", "--outdir", required=True, help="Output directory for NanoPlot results")
    parser.add_argument("-t", "--threads", type=int, default=8, help="Number of threads (default=8)")
    args = parser.parse_args()

    run_nanoplot(args.fastq, args.outdir, args.threads)