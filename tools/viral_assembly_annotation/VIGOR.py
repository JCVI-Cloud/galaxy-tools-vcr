#!/usr/bin/env python

"""
Runs VIGOR3 and command-line VICVB on given input fasta file.
"""

import os, sys, subprocess, tempfile, shutil, re

def __main__():
	# Parse the command line options and get the current working directory in galaxy (location in which galaxy will work on this job)
	(inputFasta,outputFASTA,outputALN,outputCDS,outputFS,outputPEP,outputRPT,outputSTATS,outputTBL,out_VCB_jbrowse,out_VCB_jbrowse_extra_files_path) = sys.argv[1:]
	currentDir = os.getcwd()
	
	# Set up output variables for all outputs EXCEPT the outputs for JBrowse (last two in parsing), those two are directly sent to galaxy, and outputFASTA.
	outputName = "output"
	outputLog = "%s/%s_log.txt"      % (currentDir,outputName)
	vigorOutputALN = "%s/%s.aln"     % (currentDir,outputName)
	vigorOutputCDS = "%s/%s.cds"     % (currentDir,outputName)
	vigorOutputFS = "%s/%s.fs"       % (currentDir,outputName)
	vigorOutputPEP = "%s/%s.pep"     % (currentDir,outputName)
	vigorOutputRPT = "%s/%s.rpt"     % (currentDir,outputName)
	vigorOutputSTATS = "%s/%s.stats" % (currentDir,outputName)
	vigorOutputTBL = "%s/%s.tbl"     % (currentDir,outputName)
	
	# Create new input FASTA (outputFASTA).
	numSeqs = 0                                # Number of sequences in input fasta.
	alter_headers = 0                          # Signal if input fasta headers need to be altered.
	oldFirstWords = []                         # Ordered list of input fasta headers' first words (whitespace-delimited).
	
	# Parse through input FASTA, counting sequences, saving each header's first word, and checking first word for any need to alter.
	inputFasta_fh = open(inputFasta, "r")
	for line in inputFasta_fh.readlines():
		if (line.startswith(">")):
			numSeqs += 1
			
			line = line.rstrip("\n")
			line = re.sub(r"> *", "", line)
			firstWord = line.split(" ")[0]
			
			# If the first word is longer than 22 chars, is the same as any of the earlier first words, or has "|", ALL headers need altering.
			if ((len(firstWord) > 22) or (firstWord in oldFirstWords) or ("|" in firstWord)):
				alter_headers = 1
			
			oldFirstWords.append(firstWord)
	inputFasta_fh.close()
	
	zeropad = len(str(numSeqs))                # Amount of zeropadding "S_" tag needs for new fasta headers.
	count = 0                                  # Order in which headers appear.
	
	# If headers need to be altered, parse through input fasta again. Print everything to outputFASTA.
	if (alter_headers):
		inputFasta_fh = open(inputFasta, "r")
		outputFASTA_fh = open(outputFASTA,"w")
		
		for line in inputFasta_fh.readlines():
			# If header read in, create new word composed of "S<zeropadded count>_<left portion of old first word>".
			# New first word can't be longer than 22 chars.
			# Create new header by inserting new word between ">" and current header.
			if (line.startswith(">")):
				count += 1
				oldHeader = line[1:]
				oldFirstWord = oldFirstWords.pop(0)
				newFirstWord = re.sub(r"\|","_",oldFirstWord)
				newFirstWord = "S%s_%s" % (str(count).rjust(zeropad,'0'),newFirstWord)
				newHeader = ">%s %s" % (newFirstWord[:22],oldHeader)
				outputFASTA_fh.write("%s" % newHeader)
			else:
				outputFASTA_fh.write(line)
		
		inputFasta_fh.close()
		outputFASTA_fh.close()
	# If not, copy input fasta to outputFASTA directly.
	else:
		subprocess.check_call("cp %s %s" % (inputFasta,outputFASTA), shell=True)
	
	subprocess.check_call("chmod 777 %s" % outputFASTA, shell=True)
	
	# Run VIGOR and copy output files to corresponding galaxy outputs
	vigorCommand = "/usr/local/VIGOR/tools/vigor/prod3/VIGOR3.pl -A -i %s -O %s/%s > %s" % (outputFASTA,currentDir,outputName,outputLog)
	subprocess.check_call((vigorCommand,), shell=True)
	subprocess.check_call("chmod 777 %s/%s.*" % (currentDir,outputName), shell=True)
	subprocess.check_call("cp %s %s" % (vigorOutputALN,outputALN), shell=True)
	subprocess.check_call("cp %s %s" % (vigorOutputCDS,outputCDS), shell=True)
	subprocess.check_call("cp %s %s" % (vigorOutputFS,outputFS), shell=True)
	subprocess.check_call("cp %s %s" % (vigorOutputPEP,outputPEP), shell=True)
	subprocess.check_call("cp %s %s" % (vigorOutputRPT,outputRPT), shell=True)
	subprocess.check_call("cp %s %s" % (vigorOutputSTATS,outputSTATS), shell=True)
	subprocess.check_call("cp %s %s" % (vigorOutputTBL,outputTBL), shell=True)
	
	# Run VICVB, submit expected galaxy output objects as the output parameters (last two in vicvb_galaxy_tool)
	vicvbCommand = "/usr/local/VICVB/vicvb_galaxy_tool to-jbrowse None '%s' '%s' '%s' '%s'" % (outputFASTA,currentDir,out_VCB_jbrowse,out_VCB_jbrowse_extra_files_path)
	subprocess.check_call((vicvbCommand,), shell=True)

if __name__=="__main__": 
	__main__()
