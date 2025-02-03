#!/usr/bin/env python3

import optparse
import os
import sys

def main(args):
  usage = ('usage: %prog [options]\n')
  parser = optparse.OptionParser(usage)
  parser.add_option('-s', '--source',
                    help='source-file to be linked.')
  parser.add_option('-t', '--target',
                    help='target_file to be linked.')
  
  (options, args) = parser.parse_args()
  
  if not options.source: 
    parser.error('Missing source.  Specify bucket with --source.')
  if not options.target: 
    parser.error('Missing bucket.  Specify bucket with --target.')

  source_file = options.source
  target_file = options.target

  # Ensure the directory containing the target link exists
  mkdir_cmd = "mkdir -p {}".format(os.path.split(target_file)[0])
  os.system(mkdir_cmd)

  link_cmd= "ln -s {} {}".format(source_file, target_file)
  print("adding symbolic link {} to system binary".format(link_cmd))
  os.system(link_cmd)

if __name__ == '__main__':
  sys.exit(main(sys.argv))
