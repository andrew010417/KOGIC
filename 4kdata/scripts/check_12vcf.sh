#!/bin/bash
# 01_check_vcf.sh
# Purpose: Check basic structure of chr12 VCF file (header + preview)
# Tool: bcftools v1.18

# VCF file path (edit if needed)
VCF=/BiO/Access/jaehyung/myfirstjob/4kdata/Korea4K.Final/chr12.recal.vcf

# 1. Check bcftools version
bcftools --version

# 2. Show first 20 lines of VCF header
bcftools view $VCF | head -n 20

# 3. Show first few variant records (exclude header)
bcftools view $VCF | grep -v "^#" | head

# 4. Extract simple variant table (for learning / inspection)
bcftools query \
-f '%CHROM\t%POS\t%ID\t%REF\t%ALT\t%INFO/AF\n' \
$VCF | head
