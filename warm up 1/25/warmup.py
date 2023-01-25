# write a python code that would take an input message of "good morning python," and convert all "o"s to "e"s.
'''
"good morning python" = input
'''
message = input("good morning")

def translate(message):
    translation=""
    for letters in message:
        if letters in "o":
            translation = translation + "e"
        else:
            translation + translation + message
            return translation

        print(translate)