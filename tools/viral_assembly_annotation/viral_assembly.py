#!/usr/bin/env python

"""
Takes input from viral_assembly.xml and sends it to viral_assembly_pipeline.py.
"""

import os, sys, subprocess, tempfile, shutil, time

def __main__():
	# Parse the command line options and get the current working directory in galaxy (location in which galaxy will work on this job)
	(input_Illumina,input_Iontorrent,input_Sanger_seqs,input_Sanger_qual,input_454,database,outputFasta) = sys.argv[1:]
	currentDir = os.getcwd()
	
	viral_assembly_cmd_files = ""
	if (input_Illumina != "None"): viral_assembly_cmd_files = "%s --input-Illumina %s " % (viral_assembly_cmd_files,input_Illumina)
	if (input_Iontorrent != "None"): viral_assembly_cmd_files = "%s --input-Iontorrent %s " % (viral_assembly_cmd_files,input_Iontorrent)
	if (input_Sanger_seqs != "None"): viral_assembly_cmd_files = "%s --input-Sanger-seqs %s " % (viral_assembly_cmd_files,input_Sanger_seqs)
	if (input_Sanger_qual != "None"): viral_assembly_cmd_files = "%s --input-Sanger-qual %s " % (viral_assembly_cmd_files,input_Sanger_qual)
	if (input_454 != "None"): viral_assembly_cmd_files = "%s --input-454 %s " % (viral_assembly_cmd_files,input_454)
	
	# If no read files provided, raise error message.
	if (viral_assembly_cmd_files == ""):
		sys.stderr.write("No read files (Illumina, Iontorrent, Sanger, or 454) were provided. At least one is required.")
		sys.exit(1)
	# Otherwise, execute the viral assembly pipeline, then copy final consensus FASTA into expected galaxy history item outputFasta.
	else:
		viral_assembly_cmd = "/usr/local/VHTNGS_new/viral_assembly_pipeline.py %s--input-Viral-DB %s --output-dir %s" % (viral_assembly_cmd_files,database,currentDir)
		viral_assembly_fasta = "%s/final/final_consensus.fasta" % currentDir
		subprocess.check_call((viral_assembly_cmd,), shell=True)
		subprocess.check_call("cp %s %s" % (viral_assembly_fasta,outputFasta), shell=True)

if __name__=="__main__": 
  __main__()
