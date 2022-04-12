#single-line comments

=begin
block comments
=end

=begin
the difference between puts and print is that
puts automarically adds a newline after every entry, while
print does not
=end

# type "irb" in the terminal to type ruby code
#command line = ruby file_name.rb

# -----WHILE/UNTIL LOOPS-----
i = 0
while i < 1
  puts i
  i += 1
end
#make sure to put an END after block codes

ii = 1
until ii > 10
  puts ii
  ii += 2
end
#excludes the limit value

# -----THE FOR LOOP-----
for num in 1...10
  puts num
end

for num in 1..10
  puts num
end
#TWO DOTS - include the highest num
#THREE DOTS - don't include highest num

# -----THE LOOP METHOD-----
value = 0
loop do
  value -= 1
  print "#{value}\n"
  break if value == -21
end
#alt + ¥ ---> \

# -----NEXT-----
i = 20
loop do
  i -= 1
  next if i % 2 == 1
  print "#{i}\n"
  break if i <= 0
end

# -----ARRAY-----
my_array = [1,2,3,4,5]
does_not_work_array = [1..5]
#second one will print as [1..5] not 1 2 3 4 5
print my_array[2]
#will print 3

#-----MULTIDIMENTIONAL ARRAY-----
multi_dim = [[0,0,0],[0,0,1],[1,2,2]]
# ^ is a 2D array
multi_dim.each{ |array|
  puts array
  #puts "#{array}\n"
}

# -----.EACH-----
my_array.each{ |number|
  x += 10
  print "#{number}"
}

my_array.each do |number|
  x += 10
  print "#{number}"
end
#1112131415 cuz each loop resets the value of number
#apply expression to each element of object one at a time like LOOP
#either use {} or do/end

#-----ITERATE OVER ARRAYS-----
numbers = [1,2,3,4,5]
numbers.each {|element| puts element}
#or
numbers.each {|element| print"#{element}\n"}

#-----.TIMES-----
12.times {
  print "crunchy bacon bits"
}
#a simpler FOR LOOP
#perform object a specified(12 in this case) num of times

# -----.SPLIT-----
text = "there you go"
words = text.split(" ")
#words = ["there", "you", "go"]
#turns string into array by dividing at delimiter

#-----ITERATE/ACCESS MULTIDIMENTIONAL ARRAYS-----
s = [["ham", "swiss"], ["turkey", "cheddar"], ["roast beef", "gruyere"]]

s.each{ |sub_array|
  sub_array.each{|array|
    puts array}}
#or
s.each do |sub_array|
  sub_array.each do |y|
    puts y
  end
end

#-----HASH-----
#you can make a hash with key-value pairs like the one below
sounds = Hash.new
sounds["doggo"] = "woof"
sounds["cat"] = "meow"
sounds["cow"] = "moo"
sounds["fox"] = "que existential crisis"
#create a new key by putting it in [] then use = to assign a value

#-----ITERATE OVER HASH-----
lunch = {
  "Conner" => "sausage",
  "Olivia" => "her gf idk",
  "Dylan" => "soup stock",
  "Colin" => "lettuce sprouts",
  "Rina" => "cotton candy"
}
lunch.each{ |menu|
  puts order[1]
}
#this prints only the right half of the hash or the "value"

#-----RUBY METHODS-----
m = Hash.new
m [".to_s"] = "turn integer into string"
m [".sort_by"] = "sort from small to big"
m [".reverse!"] = "reverse the order of any list or string permanently"
m [".reverse"] = "same as reverse! but keeps the input array as is"
m [".split"] =
m [".include? "smth" "] = "looks for parameter in the string"
