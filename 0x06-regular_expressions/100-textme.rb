#!/usr/bin/env ruby
print ARGV[0].scan(/\[from:(.*?)\]/),
      ARGV[0].scan(/\[to:(.*?)\]/),
      ARGV[0].scan(/\[flags:(.*?)\]/).join
print(",")

