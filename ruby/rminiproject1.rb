
puts "Tell me a secret: "
text = gets.chomp
puts "What words would you want to keep secret?: "
redact = gets.chomp

words = text.split(" ")

words.each do |word|
  if word == redact
    print "REDACTED "
  else
    print word + " "
  end
end
