#!/usr/bin/env python

"""
Runs VIGOR3 on given input fasta file.
"""

import os, sys, subprocess, tempfile, shutil

def __main__():
	# Parse the command line options
	(inputFasta,outputALN,outputCDS,outputFS,outputPEP,outputRPT,outputSTATS,outputTBL) = sys.argv[1:]
	
	# Set up output variables
	outputDir = "/usr/local/tools/vigor/output"
	outputName = "output"
	vigorOutputALN = "%s/%s.aln"     % (outputDir,outputName)
	vigorOutputCDS = "%s/%s.cds"     % (outputDir,outputName)
	vigorOutputFS = "%s/%s.fs"       % (outputDir,outputName)
	vigorOutputPEP = "%s/%s.pep"     % (outputDir,outputName)
	vigorOutputRPT = "%s/%s.rpt"     % (outputDir,outputName)
	vigorOutputSTATS = "%s/%s.stats" % (outputDir,outputName)
	vigorOutputTBL = "%s/%s.tbl"     % (outputDir,outputName)
	
	# Run command
	command = "/usr/local/tools/vigor/prod3/VIGOR3.pl -A -i %s -O %s/%s > %s/%s_log.txt" % (inputFasta,outputDir,outputName,outputDir,outputName)
	os.system("sudo %s" % command)
	os.system("sudo chmod 777 %s/%s.*" % (outputDir,outputName))
	os.system("sudo cp %s %s" % (vigorOutputALN,outputALN))
	os.system("sudo cp %s %s" % (vigorOutputCDS,outputCDS))
	os.system("sudo cp %s %s" % (vigorOutputFS,outputFS))
	os.system("sudo cp %s %s" % (vigorOutputPEP,outputPEP))
	os.system("sudo cp %s %s" % (vigorOutputRPT,outputRPT))
	os.system("sudo cp %s %s" % (vigorOutputSTATS,outputSTATS))
	os.system("sudo cp %s %s" % (vigorOutputTBL,outputTBL))

if __name__=="__main__": 
	__main__()
