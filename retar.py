import sys
import os
import tempfile
import shutil
from subprocess import call

def main(args):
    archive_name = args[1]
    orig_archive_name = archive_name + ".orig"

    os.rename(archive_name, orig_archive_name)
    temp_dir = tempfile.mkdtemp()

    print archive_name
    print orig_archive_name
    print temp_dir

    call(["tar", "-xzf", orig_archive_name, "-C", temp_dir])

    dirs_inside = [os.path.join(temp_dir, d)
                   for d in os.listdir(temp_dir)
                   if os.path.isdir(os.path.join(temp_dir, d))]

    print dirs_inside

    zookeeper_dir = dirs_inside[0]

    call(["tar", "-czf", archive_name, "-C", zookeeper_dir, "."])

    shutil.rmtree(temp_dir)


if __name__ == "__main__":
    main(sys.argv)
