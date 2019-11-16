import os, csv, sys
from shutil import copyfile

if sys.version_info[0] < 3:
    print("This script must be run with python 3.")
    if len(sys.argv) < 2:
        raw_input("press enter to exit")
    sys.exit()

try:
    import zstandard as zstd
except ImportError:
    answer = input("zstandard is required to run this script.\nTry to install it? (Y/N) ").lower()
    if(answer == "y" or  answer == "yes"):
            # This is kinda gross, but it might help the illiterate
            os.system('py -' + str(sys.version_info[0]) + ' -m pip install zstandard')
            os.system('python' + str(sys.version_info[0]) + ' -m pip install zstandard')
            import zstandard as zstd
    else:
        sys.exit()

hexChars = "1234567890ABCDEFabcdef"
# borrowed from https://github.com/Birdwards/SmashPad
def decomp(input_name, output_name):
    o = open(output_name, 'w+b')
    i = open(input_name, 'rb').read()
    dctx = zstd.ZstdDecompressor()
    for chunk in dctx.read_to_iter(i):
        o.write(chunk)
    n = o.tell()
    o.close()
    print("Output file to: \"" + os.path.abspath(output_name) + "\"")

if len(sys.argv) < 2:
    modDir = input("Input the path to a mod folder (dragging a folder into the window will input its path)\n")
    modDir = modDir.strip('\"')
    #sys.exit("Please provide a mod directory and arc version as arguments")
else:
    modDir = sys.argv[1]
if len(sys.argv) < 3:
    arcVersion = input("what version do these offsets correspond to?\n")
else:
    arcVersion = sys.argv[2]
outputBase = os.path.join("output", os.path.basename(modDir))

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Offsets " + arcVersion + ".txt"), "r") as offsetsFile:
    for root, dirs, files in os.walk(modDir, False):
        offsetsFile.seek(0)
        next(offsetsFile)  # skip metadata line
        for line in offsetsFile:
            fileInfo = line.split(",")
            arcPath = fileInfo[0]
            offset = fileInfo[1]
            for fileName in files:
                offsetPos = fileName.find(offset)
                if offsetPos != -1 and ((offsetPos + len(offset) <= len(fileName) or fileName[offsetPos + len(offset)] not in hexChars) and (offsetPos == 0 or fileName[offsetPos - 1] not in hexChars)):
                    filePath = os.path.normpath(os.path.join(root, fileName))
                    outPath = os.path.normpath(os.path.join(outputBase, arcPath))
                    os.makedirs(os.path.dirname(outPath), 0o777, True)
                    try:
                        decomp(filePath, outPath)
                    # if the file can't be decompressed, copy instead
                    except zstd.ZstdError:
                        copyfile(filePath, outPath)
                    files.remove(fileName)
if len(sys.argv) < 2:
    input("press enter to exit")
