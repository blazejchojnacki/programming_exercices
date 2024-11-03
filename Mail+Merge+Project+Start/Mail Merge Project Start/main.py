#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("Input/Names/invited_names.txt") as names:
    name_list = names.readlines()
    # print(name_list)
    for each_name in name_list:
        with open("Input/Letters/starting_letter.txt") as letter:
            letter_content = letter.read()
            mail_content = letter_content.replace("[name]", each_name.strip())
            # print(mail_content)
            # breakpoint()
            with open(f"Output/ReadyToSend/Letter_for_{each_name.strip()}.txt", "w") as mail:
                mail.write(mail_content)

