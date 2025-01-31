import re

#RELEVANT FILE NAMES
input_file = "input_text.txt"
output_file = "redacted_text.txt"

bad_words = "toredact.txt"


#READ IN PRONOUNS
pronoun_file = open(bad_words, "r") 
pronoun_data = pronoun_file.read()
pronoun_file.close()

pronoun_list = pronoun_data.replace('\n', ' ').split(" ")

#READ IN TEXT
text_file = open(input_file, "r") 
text_data = text_file.read() 
text_file.close()

#REDACT DATA
outstring = text_data

for pronoun in pronoun_list:
    length = len(pronoun)
    red = string_val = "█" * length  # gives you "xxxxxxxxxx"
    pronoun_nocase = re.compile(re.escape(pronoun), re.IGNORECASE)
    outstring = pronoun_nocase.sub(red, outstring)

#WRITE TO NEW FILE
with open(output_file, "w") as f:
    f.write(outstring)
f.close()
