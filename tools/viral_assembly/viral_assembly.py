#!/usr/bin/python

import os.path
import sys
import optparse

if __name__ == "__main__":
  main()

def main():

  # Parse the command line options
  usage = "Usage: vir-assembly-pipeline.sh <SFF of 454> <FASTA of Sanger> <FASTQ of Solexa> <tab-delimited of Solexa trimpoints> <database>"
  parser = optparse.OptionParser(usage = usage)
  parser.add_option("--input_454",
                    action="append", type="string",
                    dest="input_454", help="input SFF file")
  parser.add_option("--input_Sanger",
                    action="store", type="string",
                    dest="input_Sanger", help="input Sanger file")
  parser.add_option("--input_Solexa",
                    action="store", type="string",
                    dest="input_Solexa", help="input Solexa file")
  parser.add_option("--input_Solexa_tp",
                    action="store", type="string",
                    dest="input_Solexa_tp", help="input Solexa trimpoints file")
  parser.add_option("--database",
		            action="store", type="string",
					dest="database", help="database")

  (options, args) = parser.parse_args()

  # Replace missing files with empty replacements.
  if options.input_454 == None:
	options.input_454 = "dummy_454.sff"
	os.system("touch %s" % options.input_454)
  if options.input_Sanger == None:
	options.input_Sanger = "dummy_Sanger.fasta"
	os.system("touch %s" % options.input_Sanger)
  if options.input_Solexa == None:
	options.input_Solexa = "dummy_Solexa.fastq"
	os.system("touch %s" % options.input_Solexa)
  if options.input_Solexa_tp == None:
	options.input_Solexa_tp = "dummy_Solexa_tp.txt"
	os.system("touch %s" % options.input_Solexa_tp)
  
  command = "/usr/local/VHTNGS/vir-assembly-pipeline.sh %s %s %s %s %s" % (options.input_454,options.input_Sanger,options.input_Solexa,options.input_Solexa_tp,database)
  os.system("echo %s >> out.txt" % command)
  
  # End the program.
  return 0
