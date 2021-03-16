#!/usr/bin/python3




import time
import os
import typing

import jk_utils
import jk_pathpatternmatcher2
import jk_terminal_essentials
import jk_uploadpack






SRC_DIR_PATH = "/home/woodoo/DevPriv/Www/www.binary-overflow.de/output/wwwroot"
OUTPUT_BASE_FILE_NAME = "pack.up"








def compress(compression:str):
	outFilePath = OUTPUT_BASE_FILE_NAME + (("." + compression) if compression else "")

	t0 = time.time()

	with jk_uploadpack.Packer(outFilePath, compression) as up:
		up.fileGroup("default").bCleanDir = True

		allFiles = []
		for e in jk_pathpatternmatcher2.walk(
				SRC_DIR_PATH,
				acceptDirPathPatterns = None,
				acceptFilePathPatterns = "**/*",
				acceptLinkPathPatterns = None,
				ignorePathPatterns = "**/__*",
				ignoreDirPathPatterns = None,
				ignoreFilePathPatterns = None,
				ignoreLinkPathPatterns = None,
				emitDirs = False,
				emitFiles = True,
				emitLinks = False,
				emitBaseDirs = False,
				recursive = True,
				sort = True,
				emitErrorEntries = True,
				clazz = None,
				ioAdapter = None,
			):

			allFiles.append((e.fullPath, e.relFilePath))

		sp = jk_terminal_essentials.Spinner(len(allFiles))
		for fullPath, relFilePath in allFiles:
			sp.spin("packing", relFilePath)
			up.fileGroup("default").addFile(fullPath, relFilePath)

	sp.hide()

	print()
	print("upload pack", compression if compression else "uncompressed")
	print()
	print("\ttotalSizeLogical =", jk_utils.formatBytes(up.totalSizeLogical))
	print("\ttotalSizeUncompressed =", jk_utils.formatBytes(up.totalSizeUncompressed))
	print("\ttotalSizeCompressed =", jk_utils.formatBytes(up.totalSizeCompressed))
	print("\tduration:", jk_utils.formatTime(time.time() - t0, withMilliseconds=True))
	print()

#



compress(None)
#compress("gz")
#compress("bz2")
#compress("xz")

