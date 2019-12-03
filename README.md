[comment]: # (This file is meant to be read with markdown formatting such as on github)

# OffsetModUpdater
Updates old, compressed, offset named ssbu mods to decompressed files named by their arc path  
You must have the offsets.txt for the version you are converting **from**.  
The arc path format is version independent, so **the version you wish to use these mods on is irrelevant** to this program.
Arguments are optional, you will be prompted for any additional required information.
If python 3 is the default on your system, the script can be ran simply by double clicking the file.

Arguments: [path to mod folder] [version that these offsets correspond to]

Example command:  
    `py -3 OffsetModUpdater.py "C:\path\to\myModFolder" 3.1.0`

Requires the zstandard library, use `py -3 -m pip install zstandard` to install it.  
If it is missing, the script can optionally attempt to run this command for you.

If using an OS other than Windows replace `py -3` with `python3` in both of the commands above.

<a href="https://github.com/Genwald/OffsetModUpdater/archive/master.zip"> <img src="https://archive.org/download/download-button-png/download-button-png.png" alt="Download" width="250"/></a>
