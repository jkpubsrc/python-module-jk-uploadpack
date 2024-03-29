jk_uploadpack
==========

Introduction
------------

This python module provides a packer/unpacker based on 'tar' that reduces redundancies before packing.

Information about this module can be found here:

* [github.org](https://github.com/jkpubsrc/python-module-jk-uploadpack)
* [pypi.python.org](https://pypi.python.org/pypi/jk_uploadpack)

Why 'uploadpack'?
----------------

Classic compression tools work very well in general. But in very specific situations these tools won't work well enough: If you need to compress data containing redundant
data that can't be compressed very well. This is the case with some directory trees for web sites hosted by webservers. And precisely that was the motivation to implement
`uploadpack`.

So `uploadpack` is nothing more than a `tar` based compression tool. In fact an `uploadpack` is nothing else but a `tar` file (possibly compressed with `gz`, `bzip2` or `xz`)
with a very specific structure: It avoids redundancies.

Limitations of this module
--------------------------

This `uploadpack` currently only suppors files and directories, no links.

Preliminaries
------------------------------------------------------------------

Please include an import statement for this module into your application by using the following code:

```python
import jk_uploadpack
```

How to compress a directory tree to an `uploadpack` archive
------------------------------------------------------------------

In order to create an `uploadpack` you need to instantiate a packer:

```python
up = jk_uploadpack.Packer("archive.up.gz")
```

Now you can create a file group (here: "foo") and add a file to it (here: "foobar.txt"):

```python
up.fileGroup("foo").addFile("/path/to/dir/foobar.txt", "dir/foobar.txt")
```

Of course you can repeat that with any number of files.

After having added all files you need to close the archive:

```python
up.close()
```

You must always invoke `close()` as otherwise essential data will not be written.

A more secure way of doing this is by using `Packer` with `with`:

```python
with jk_uploadpack.Packer("archive.up.gz") as up:
	up.fileGroup("foo").addFile("/path/to/dir/foobar.txt", "dir/foobar.txt")
```

In this case `close()` will be called automatically.

How to uncompress an `uploadpack` archive
------------------------------------------------------------------

In order to decompress an `uploadpack` you need to instantiate an unpacker:

```python
up = jk_uploadpack.Unpacker("archive.up.gz")
```

Then you can unpack all files to a target directory:

```python
up.fileGroup("default").unpackToDir("outdir")
```

After having extracted all files you can close the archive:

```python
up.close()
```

You should always invoke `close()`.

A more secure way of doing this is by using `Unpacker` with `with`:

```python
with jk_uploadpack.Unpacker("archive.up.gz") as up:
	up.fileGroup("default").unpackToDir("outdir")
```

In this case `close()` will be called automatically.

Specific Features
--------------------------------------

### File Groups

`uploadpack` always puts files in so called file groups. File groups are organizational units that can be considered as being an archive themselves. Characterstics of such a file group are:

* A file group is identified by a name.
* On decompression all files of a file group are always written to a specific directory.
* Certain parameters can be set at a file group that take effect for all files in that file group.

If you don't need to use file groups for a specific reason, use "`default`" as a convention.

Contact Information
-------------------

Author(s):

* Jürgen Knauth: pubsrc@binary-overflow.de

License
-------

This software is provided under the following license:

* Apache Software License 2.0



