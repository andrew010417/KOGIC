#마스터 스크립트 사용법
python check_hifiQC.py \
    -f reads.fastq \
    -b reads.ccs.bam \
    -o /path/to/output \
    -t 8
(-t : 스레드 수 (NanoPlot용, 기본 8))

#단독 함수 import 사용법
from hifi_qc_module import run_nanoplot, check_rq

# NanoPlot
run_nanoplot("reads.fastq", "out_dir/NanoPlot", threads=8)

# RQ QC
check_rq("reads.ccs.bam", "out_dir/RQ_results.txt", "out_dir/RQ_histogram.png")