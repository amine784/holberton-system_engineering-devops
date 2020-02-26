#!/usr/bin/env ruby
reg = (.*?)\
puts ARGV[0].scan(/\[from:reg] \[to:reg] \[flags:reg]/).join(",")


