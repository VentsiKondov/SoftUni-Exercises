command= input()


while command != 'End':
    final_sentence = ""
    if command != 'SoftUni':
        for char in command:
            final_sentence += 2 * char


        print(final_sentence)
    command = input()


