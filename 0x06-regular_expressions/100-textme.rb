#!/usr/bin/env ruby
print ARGV[0].scan(/\[from:(.*?)\]/),
      print ARGV[0].scan(/\[to:(.*?)\]/),
            print ARGV[0].scan(/\[flags:(.*?)\]/).join
print(",")

