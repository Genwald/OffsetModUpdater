# OffsetModUpdater
Updates old, compressed, offset named ssbu mods to decompressed files named by their arc path  
You must have the offsets.txt for the version you are converting from.  
The arc path format is version independent, so the version you wish to use these mods on is irrelevant to this program.

Arguments: [path to mod folder] [version that these offsets correspond to]

Example command:  
    <p>`py -3 OffsetModUpdater.py myModFolder 3.1.0`</p>

Requires the zstandard library, use `pip install zstandard` to install it.
