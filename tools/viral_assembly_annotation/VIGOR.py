#!/usr/bin/env python

"""
Runs VIGOR3 and command-line VICVB on given input fasta file.
"""

import os, sys, subprocess, tempfile, shutil

def __main__():
	# Parse the command line options and get the current working directory in galaxy (location in which galaxy will work on this job)
	(inputFasta,outputALN,outputCDS,outputFS,outputPEP,outputRPT,outputSTATS,outputTBL,out_VCB_jbrowse,out_VCB_jbrowse_extra_files_path) = sys.argv[1:]
	currentDir = os.getcwd()
	
	# Set up output variables for all outputs EXCEPT the outputs for JBrowse (last two in parsing), those two are directly sent to galaxy
	outputName = "output"
	outputLog = "%s/%s_log.txt"      % (currentDir,outputName)
	vigorOutputALN = "%s/%s.aln"     % (currentDir,outputName)
	vigorOutputCDS = "%s/%s.cds"     % (currentDir,outputName)
	vigorOutputFS = "%s/%s.fs"       % (currentDir,outputName)
	vigorOutputPEP = "%s/%s.pep"     % (currentDir,outputName)
	vigorOutputRPT = "%s/%s.rpt"     % (currentDir,outputName)
	vigorOutputSTATS = "%s/%s.stats" % (currentDir,outputName)
	vigorOutputTBL = "%s/%s.tbl"     % (currentDir,outputName)
	
	# Run VIGOR and copy output files to corresponding galaxy outputs
	vigorCommand = "/usr/local/VIGOR/tools/vigor/prod3/VIGOR3.pl -A -i %s -O %s/%s > %s" % (inputFasta,currentDir,outputName,outputLog)
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
	vicvbCommand = "/usr/local/VICVB/vicvb_galaxy_tool to-jbrowse None '%s' '%s' '%s' '%s'" % (inputFasta,currentDir,out_VCB_jbrowse,out_VCB_jbrowse_extra_files_path)
	subprocess.check_call((vicvbCommand,), shell=True)

if __name__=="__main__": 
	__main__()
