#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import pysam

# -----------------------------
# 사용자 설정
# -----------------------------
BAM = "/BiO/Research/Project1/PGP1_iPSC_assembly/Resources/TBD251228_25180/01.RawData/PGP1/PGP1.hifi_reads.bam"
FASTQ = "/BiO/Research/Project1/PGP1_iPSC_assembly/Resources/TBD251228_25180/01.RawData/PGP1/PGP1.hifi_reads.fastq.gz"
OUTDIR = "/BiO/Research/Project1/PGP1_iPSC_assembly/Results/QC_results/Hifi_QC"
RQ_OUT = os.path.join(OUTDIR, "hiqc_rq_result.txt")

# 필요시 폴더 생성
os.makedirs(OUTDIR, exist_ok=True)

# -----------------------------
# 1️⃣ RQ QC
# -----------------------------
def rq_qc(bam_file, out_file):
    total = 0
    good = 0
    # BAM 파일 열기
    with pysam.AlignmentFile(bam_file, "rb") as bam:
        for read in bam:
            # 태그 가져오기
            if read.has_tag("rq"):
                rq = read.get_tag("rq")  # float
                total += 1
                if rq >= 0.99:
                    good += 1

    fraction = good / total if total > 0 else 0
    # 결과 저장
    with open(out_file, "w") as f:
        f.write(f"total RQ tags = {total}\n")
        f.write(f"good RQ tags (>=0.99) = {good}\n")
        f.write(f"fraction = {fraction}\n")

    print(f"[RQ QC] Done! Results saved to {out_file}")

# -----------------------------
# 2️⃣ NanoPlot QC
# -----------------------------
def nanoplot_qc(fastq_file, out_dir, threads=8):
    cmd = [
        "NanoPlot",
        "--fastq", fastq_file,
        "--threads", str(threads),
        "--outdir", out_dir
    ]
    print(f"[NanoPlot] Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)
    print(f"[NanoPlot] Done! Results in {out_dir}")

# -----------------------------
# 메인 실행
# -----------------------------
if __name__ == "__main__":
    print("=== HiFi QC Script Start ===")
    rq_qc(BAM, RQ_OUT)
    nanoplot_qc(FASTQ, OUTDIR)
    print("=== HiFi QC Script End ===")