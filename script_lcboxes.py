#!/bin/bash
#
# COMMENT  Your job name
#$ -N make_lcboxes_244_8.2S
# COMMENT  Run job through bash shell
#$ -S /bin/bash
# COMMENT define mail notification events (b,e,n,s)
#$ -m bes
# COMMENT set mail notification never
##$ -m n
# COMMENT who to mail
#$ -M kd242@sussex.ac.uk
# COMMENT reference from current working directory
#$ -cwd
# COMMENT Name output and error files if you want
##$ -o 
##$ -e 
# COMMENT specify the queue
##$ -q pact_long.q
#$ -q mps.q
# COMMENT  pe (Parallel environment) request. Set your number of processors here.
##$ -pe openmpi 32
# COMMENT catch kill and suspend signals
#$ -notify

# COMMENT  If modules are needed, source modules environment:
. /etc/profile.d/modules.sh
module load python/2.7.5
module load intel/parallel_studio_xe/2013/14.0.1

# COMMENT run your program
python make_lcboxes.py
