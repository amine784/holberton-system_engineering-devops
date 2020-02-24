#!/usr/bin/env ruby
from = print ARGV[0].scan(/\[from:(.*?)\]/).join
to = print ARGV[0].scan(/\[to:(.*?)\]/).join
flags = print ARGV[0].scan(/\[flags:(.*?)\]/).join
dlm = ","
print from + delm + to + delm + flags
