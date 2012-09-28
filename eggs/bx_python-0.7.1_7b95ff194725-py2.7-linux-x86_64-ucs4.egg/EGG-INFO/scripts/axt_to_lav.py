#!/afs/bx.psu.edu/project/pythons/linux-x86_64-ucs4/bin/python2.7

"""
Application to convert AXT file to LAV file. Reads an AXT file from standard 
input and writes a LAV file to standard out; some statistics are written to 
standard error.

usage: %prog primary_spec secondary_spec [--silent] < axt_file > lav_file

Each spec is of the form seq_file[:species_name]:lengths_file.

- seq_file should be a format string for the file names for the individual
  sequences, with %s to be replaced by the alignment's src field.  For 
  example, "hg18/%s.nib" would prescribe files named "hg18/chr1.nib", 
  "hg18/chr2.nib", etc.

- species_name is optional.  If present, it is prepended to the alignment's 
  src field.

- Lengths files provide the length of each chromosome (lav format needs this
  information but axt file does not contain it).  The format is a series of
  lines of the form:

  <chromosome name> <length>

  The chromosome field in each axt block must match some <chromosome name> in
  the lengths file.
"""

__author__ = "Bob Harris (rsharris@bx.psu.edu)"

import sys
import copy
import bx.align.axt
import bx.align.lav


def usage(s=None):
	message = __doc__
	if (s == None): sys.exit (message)
	else:           sys.exit ("%s\n%s" % (s,message))


def main():
	global debug

	# parse the command line

	primary   = None
	secondary = None
	silent    = False

	# pick off options

	args = sys.argv[1:]
	while (len(args) > 0):
		arg = args.pop(0)
		val = None
		fields = arg.split("=",1)
		if (len(fields) == 2):
			arg = fields[0]
			val = fields[1]
			if (val == ""):
				usage("missing a value in %s=" % arg)

		if (arg == "--silent") and (val == None):
			silent = True
		elif (primary == None) and (val == None):
			primary = arg
		elif (secondary == None) and (val == None):
			secondary = arg
		else:
			usage("unknown argument: %s" % arg)

	if (primary == None):
		usage("missing primary file name and length")

	if (secondary == None):
		usage("missing secondary file name and length")

	try:
		(primaryFile,primary,primaryLengths) = parse_spec(primary)
	except:
		usage("bad primary spec (must be seq_file[:species_name]:lengths_file")

	try:
		(secondaryFile,secondary,secondaryLengths) = parse_spec(secondary)
	except:
		usage("bad secondary spec (must be seq_file[:species_name]:lengths_file")

	# read the lengths

	speciesToLengths = {}
	speciesToLengths[primary]   = read_lengths (primaryLengths)
	speciesToLengths[secondary] = read_lengths (secondaryLengths)

	# read the alignments

	out = bx.align.lav.Writer(sys.stdout, \
			attributes = { "name_format_1" : primaryFile,
			               "name_format_2" : secondaryFile })

	axtsRead = 0
	axtsWritten = 0
	for axtBlock in bx.align.axt.Reader(sys.stdin, \
			species_to_lengths = speciesToLengths,
			species1           = primary,
			species2           = secondary,
			support_ids        = True):
		axtsRead += 1
		out.write (axtBlock)
		axtsWritten += 1

	out.close()

	if (not silent):
		sys.stderr.write ("%d blocks read, %d written\n" % (axtsRead,axtsWritten))

def parse_spec(spec): # returns (seq_file,species_name,lengths_file)
	fields = spec.split(":")
	if   (len(fields) == 2): return (fields[0],"",fields[1])
	elif (len(fields) == 3): return (fields[0],fields[1],fields[2])
	else:                    raise ValueError

def read_lengths (fileName):

	chromToLength = {}

	f = file (fileName, "r")

	for lineNumber,line in enumerate(f):
		line = line.strip()
		if (line == ""): continue
		if (line.startswith("#")): continue

		fields = line.split ()
		if (len(fields) != 2):
			raise "bad lengths line (%s:%d): %s" % (fileName,lineNumber,line)

		chrom = fields[0]
		try:
			length = int(fields[1])
		except:
			raise "bad lengths line (%s:%d): %s" % (fileName,lineNumber,line)

		if (chrom in chromToLength):
			raise "%s appears more than once (%s:%d): %s" \
			    % (chrom,fileName,lineNumber)

		chromToLength[chrom] = length

	f.close ()

	return chromToLength


if __name__ == "__main__": main()

