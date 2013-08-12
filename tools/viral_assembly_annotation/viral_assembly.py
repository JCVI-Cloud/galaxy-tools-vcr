#!/usr/bin/env python

"""
Takes input from viral_assembly.xml and sends it to vir-assembly-pipeline.sh.
"""

import os, sys, subprocess, tempfile, shutil

def __prepare_input__(draftFilename,finalFilename,finalDir):
	result = "%s/%s" % (finalDir,finalFilename)
	
	if draftFilename == "None":
		subprocess.check_call("rm -f %s" % result, shell=True)
		subprocess.check_call("touch %s" % result, shell=True)
	else:
		subprocess.check_call("cp %s %s" % (draftFilename,result), shell=True)
	
	return result

def __main__():
	# Parse the command line options and get the current working directory in galaxy (location in which galaxy will work on this job)
	(input_454,input_Sanger,input_Solexa,database,outputFasta) = sys.argv[1:]
	currentDir = os.getcwd()
	
	# Copy the input files to the current location, creating empty dummy files for those inputs not given by user (required for viral assembly)
	input_454_ready = __prepare_input__(input_454,"input_454.sff",currentDir)
	input_Sanger_ready = __prepare_input__(input_Sanger,"input_Sanger.fasta",currentDir)
	input_Solexa_ready = __prepare_input__(input_Solexa,"input_Solexa.fastq",currentDir)
	
	# Execute the viral assembly pipeline, then copy final consensus FASTA into expected galaxy history item outputFasta.
	virAssemblyCommand = "/usr/local/VHTNGS/vir-assembly-pipeline.sh %s %s %s %s %s" % (input_454_ready,input_Sanger_ready,input_Solexa_ready,database,currentDir)
	virAssemblyOutput = "%s/mapping/sample_hybrid_edited_refs_consensus.fasta" % currentDir
	subprocess.check_call((virAssemblyCommand,), shell=True)
	subprocess.check_call("cp %s %s" % (virAssemblyOutput,outputFasta), shell=True)

if __name__=="__main__": 
  __main__()
