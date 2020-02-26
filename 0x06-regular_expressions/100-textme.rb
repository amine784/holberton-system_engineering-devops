#!/usr/bin/env ruby
reg = (.*?\)
delim = ","
puts ARGV[0].scan(/\[from:reg] \[to:reg] \[flags:reg]/).join(delim)


