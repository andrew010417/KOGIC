#!/bin/bash
# ============================================
# ALDH2 rs671 변이 추출 스크립트
# ============================================

# bcftools 실행 파일 절대경로
BCFTOOLS="/BiO/Access/jaehyung/tools/bcftools-1.18/bcftools"
# ↑ PATH 안 타도 항상 실행 가능

# chr12 VCF 파일
VCF="/BiO/Access/jaehyung/myfirstjob/4kdata/Korea4K.Final/chr12.recal.vcf"

# 출력 파일
OUT="results/rs671.vcf"

# rs671만 추출
$BCFTOOLS view -i 'ID=="rs671"' $VCF > $OUT
