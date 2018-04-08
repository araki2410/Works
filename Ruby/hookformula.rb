#!/usr/bin/ruby
# -*- coding:utf-8 -*-

print"Enter length:"
n = gets.to_i
#stntab = Array.new(n) { Array.new(n)}
#stntab = Array.new(n)
@stntab = Array.new()
@pear = Array.new()
jun = []
lnum = 1

def shaping(j, k, num, count)
  ch = 0
  if @stntab[k] == nil then
    @stntab[k] = []
    @pear[k] = []
  end
  # if @stntab[k][j] = nil then
  #   @stntab[k][j] = []
  # end
#########
  if @stntab[k][j].to_i == 0 then
    @stntab[k][j] = num
    @pear[k][j] = count
  elsif num > @stntab[k][j].to_i then
    if @stntab[k][j+1] == 0 then
      @stntab[k][j+1] = num
      @pear[k][j+1] = count
    else
      shaping(j+1,k,num, count)
    end
  elsif @stntab[k][j].to_i > num then
    stack = @stntab[k][j]
    @stntab[k][j] = num
    shaping(0,k+1,stack,count)
  end
#########
end





while n > 0 do
  jun << n
  n -= 1
end
jun = jun.reverse.permutation.to_a

for i in jun
  print "\n", i, "\n"
  x, y = 0, 0
  @stntab=[]
  times = 1
  for number in i
    shaping(x, y, number, times)
    times += 1
  end
  printf("%d個目ができたよー\n",lnum)
  print @stntab , "\n"
  print @pear , "\n"
  lnum += 1
end
