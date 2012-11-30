#!/usr/bin/env python

"""
Takes input from viral_assembly.xml and sends it to vir-assembly-pipeline.sh.
"""

import os, sys, subprocess, tempfile, shutil

def __prepare_input__(draftFilename,finalFilename,finalDir):
	result = "%s/%s" % (finalDir,finalFilename)
	
	if draftFilename == "None":
		os.system("sudo touch %s" % result)
	else:
		os.system("sudo cp %s %s" % (draftFilename,result))
	
	return result

def __main__():
	# Parse the command line options
	(input_454,input_Sanger,input_Solexa,input_Solexa_tp,database,outputFasta) = sys.argv[1:]
	
	# Copy the input files to the VHTNGS location. If an input file was not given, create an empty dummy file as a replacement.
	inputDir = "/usr/local/VHTNGS"
	
	input_454_ready = __prepare_input__(input_454,"input_454.sff",inputDir)
	input_Sanger_ready = __prepare_input__(input_Sanger,"input_Sanger.fasta",inputDir)
	input_Solexa_ready = __prepare_input__(input_Solexa,"input_Solexa.fastq",inputDir)
	input_Solexa_tp_ready = __prepare_input__(input_Solexa_tp,"input_Solexa.fastq.trimpoints",inputDir)
	
	command = "/usr/local/VHTNGS/vir-assembly-pipeline.sh %s %s %s %s %s" % (input_454_ready,input_Sanger_ready,input_Solexa_ready,input_Solexa_tp_ready,database)
	virAssemblyOutput = "/usr/local/VHTNGS/project/mapping/sample_hybrid_edited_refs_consensus.fasta"
	os.system("sudo %s" % command)
	os.system("sudo chmod 777 %s" % virAssemblyOutput)
	os.system("sudo cp %s %s" % (virAssemblyOutput,outputFasta))

if __name__=="__main__": 
  __main__()
