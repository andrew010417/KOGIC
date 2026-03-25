#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse
from hifi_qc_module import run_nanoplot, check_rq

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Master script for HiFi QC")
    parser.add_argument("-f", "--fastq", help="Input FASTQ for NanoPlot")
    parser.add_argument("-b", "--bam", help="Input BAM for RQ check")
    parser.add_argument("-o", "--outdir", required=True, help="Output directory")
    parser.add_argument("-t", "--threads", type=int, default=8)
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    if args.fastq:
        nanoplot_out = os.path.join(args.outdir, "NanoPlot")
        run_nanoplot(args.fastq, nanoplot_out, args.threads)

    if args.bam:
        rq_txt = os.path.join(args.outdir, "RQ_results.txt")
        rq_hist = os.path.join(args.outdir, "RQ_histogram.png")
        check_rq(args.bam, rq_txt, rq_hist)

    print("[MASTER] HiFi QC finished!")