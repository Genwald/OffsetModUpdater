import os, csv, sys
from shutil import copyfile
import zstandard as zstd

# barrowed from https://github.com/Birdwards/SmashPad
def decomp(input_name, output_name):
    o = open(output_name, 'w+b')
    i = open(input_name, 'rb').read()
    dctx = zstd.ZstdDecompressor()
    for chunk in dctx.read_to_iter(i):
        o.write(chunk)
    n = o.tell()
    o.close()
    print(output_name + "\nsuccessfully decompressed to " + hex(n) + " bytes!")


if len(sys.argv) < 2:
    sys.exit("Please provide a mod directory and arc version as arguments")
modDir = sys.argv[1]
arcVersion = sys.argv[2]
outputBase = os.path.join("output", os.path.basename(modDir))

with open("Offsets " + arcVersion + ".txt", "r") as offsetsFile:
    for root, dirs, files in os.walk(modDir, False):
        offsetsFile.seek(0)
        next(offsetsFile)  # skip metadata line
        for line in offsetsFile:
            fileInfo = line.split(",")
            arcPath = fileInfo[0]
            offset = fileInfo[1]
            for fileName in files:
                if offset in fileName:
                    filePath = os.path.normpath(os.path.join(root, fileName))
                    outPath = os.path.normpath(os.path.join(outputBase, arcPath))
                    os.makedirs(os.path.dirname(outPath), 0o777, True)
                    try:
                        decomp(filePath, outPath)
                    # if the file can't be decompressed, copy instead
                    except zstd.ZstdError:
                        copyfile(filePath, outPath)
                    files.remove(fileName)
