#!/usr/bin/env python

"""
Runs VIGOR3 on given input fasta file.
"""

import os, sys, subprocess, tempfile, shutil

def __main__():
  # Parse the command line options
  
  (input_fasta,output_txt) = sys.argv[1:]
  
  command = "/usr/local/tools/vigor/prod3/VIGOR3.pl -A -i %s -O /usr/local/tools/vigor/prod3/vigorscratch/output > /usr/local/tools/vigor/prod3/vigorscratch/output_log_data.log AND %s" % (input_fasta,output_txt)
  os.system("echo '%s' >> %s" % (command,output_txt))
  #os.system("echo '%s' >> /usr/local/tools/vigor/VIGOR.out" % command)

if __name__=="__main__": 
  __main__()
