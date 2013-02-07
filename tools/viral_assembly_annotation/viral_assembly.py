#!/usr/bin/env python

"""
Takes input from viral_assembly.xml and sends it to vir-assembly-pipeline.sh.
"""

import os, sys, subprocess, tempfile, shutil, datetime

def __prepare_input__(draftFilename,finalFilename,finalDir):
	result = "%s/%s" % (finalDir,finalFilename)
	
	if draftFilename == "None":
		os.system("sudo touch %s" % result)
	else:
		os.system("sudo cp %s %s" % (draftFilename,result))
	
	return result

def __main__():
	# Parse the command line options and acquire time.
	(input_454,input_Sanger,input_Solexa,input_Solexa_tp,database,outputFasta) = sys.argv[1:]
	time = datetime.datetime.now()
	
	# Set up relevant directories for viral assembly.
	mainDir = "/usr/local/VHTNGS"
	outputTime = time.strftime("%Y-%m-%d_%H-%M-%S")
	outputDirPath = "%s/project/%s" % (mainDir,outputTime)
	outLog = "%s/project/viral_assembly_%s.log" % (mainDir,outputTime)
	
	# Copy the input files to the VHTNGS location. If an input file was not given, create an empty dummy file as a replacement.
	os.system("sudo rm -f %s/input_454.sff" % mainDir)
	os.system("sudo rm -f %s/input_Sanger.fasta" % mainDir)
	os.system("sudo rm -f %s/input_Solexa.fastq" % mainDir)
	os.system("sudo rm -f %s/input_Solexa.fastq.trimpoints" % mainDir)
	
	input_454_ready = __prepare_input__(input_454,"input_454.sff",mainDir)
	input_Sanger_ready = __prepare_input__(input_Sanger,"input_Sanger.fasta",mainDir)
	input_Solexa_ready = __prepare_input__(input_Solexa,"input_Solexa.fastq",mainDir)
	input_Solexa_tp_ready = __prepare_input__(input_Solexa_tp,"input_Solexa.fastq.trimpoints",mainDir)
	
	# Set up command and output structure.	
	command = "%s/vir-assembly-pipeline.sh %s %s %s %s %s %s" % (mainDir,input_454_ready,input_Sanger_ready,input_Solexa_ready,input_Solexa_tp_ready,database,outputTime)
	virAssemblyOutput = "%s/mapping/sample_hybrid_edited_refs_consensus.fasta" % outputDirPath
	os.system("sudo touch %s" % outLog)
	os.system("sudo chmod 777 %s" % outLog)
	
	# Execute command and move final output to galaxy output area.
	outLogFH = open(outLog,"a")
	subprocess.call("sudo %s" % command,shell=True,stdout=outLogFH,stderr=subprocess.STDOUT)
	outLogFH.close()
	os.system("sudo chmod 777 %s" % virAssemblyOutput)
	os.system("sudo cp %s %s" % (virAssemblyOutput,outputFasta))

if __name__=="__main__": 
  __main__()
