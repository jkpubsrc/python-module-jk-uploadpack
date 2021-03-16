#!/usr/bin/python3




import time
import os
import typing

import jk_utils
import jk_terminal_essentials
import jk_uploadpack






INPUT_FILE_NAME = "pack.up"



with jk_uploadpack.Unpacker(INPUT_FILE_NAME) as up:
	sp = jk_terminal_essentials.Spinner(len(up.fileGroup("default").files))
	up.fileGroup("default").unpackToDir("out", sp)

sp.hide()

print()
print("totalSizePacked =", jk_utils.formatBytes(up.totalSizePacked))
print("totalSizeUnpacked =", jk_utils.formatBytes(up.totalSizeUnpacked))
print()


