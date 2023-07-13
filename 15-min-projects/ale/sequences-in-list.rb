# find the lenght of increasing / decreasing sequences in a list.
# [1, 2, 3, 4, 3, 2, 4, 6] -> [4, 3, 3]
# if a list begins with a repetition, it is considered to be decreasing.

def get_sequences_length(numbers)
    result = []
    previous = numbers[0]
    count = 1
    direction = ''
    numbers.slice(1..).each do |x|
        if x == previous
            if direction == ''
                direction = 'down'
            end
            count += 1
        elsif x < previous
            if direction == ''
                direction = 'down'
            end
            if direction == 'down'
                count += 1
            else
                result << count
                direction = 'down'
                count = 2
            end
        else
            if direction == ''
                direction = 'up'
            end
            if direction == 'up'
                count += 1
            else
                result << count
                direction = 'up'
                count = 2
            end
        end
        previous = x
    end
    result << count
    return result
end

numbers = [1,2,3,4,3,2,4,6]

puts get_sequences_length(numbers)
