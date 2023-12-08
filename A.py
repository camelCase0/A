import re

def undo_preceding(boring_secondary, examinations_ted):
    assure = ''
    regularlysms = boring_secondary.split('S')
    for id in range(len(regularlysms)):
        assure += chr(int(float(regularlysms[id]) - examinations_ted))
    
    return assure

def undo_string(input_string):
    pattern = r"UndoPreceding\(\"([^\"]+)\",(\d+\/?\d?)\)"
    print(f"'{input_string}'")
    matches = re.search(pattern, input_string)
    encoded_string = matches.group(1)
    number = matches.group(2)
    number = eval(number)
    print("Encoded String:", encoded_string)
    print("Number:", number)
    return undo_preceding(encoded_string, number)

def find_and_replace(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        pattern = r'UndoPreceding\(\"[^\"]+\",[^)]+\)'
        matches = re.finditer(pattern, content)

        for match in matches:
            original_string = match.group(0)
            processed_result = undo_string(match.group(0))
            content = content.replace(original_string, f'"{processed_result}"')

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

find_and_replace("B")
# boring_secondary_example = "106S129S124S109S99"
# examinations_ted_example = 32/4
# result = undo_string('(UndoPreceding("115S109S122S118S109S116S59S58S54S108S116S116",72/9))')
# print(f'"{result}"')

# Given hexadecimal string
# MagazinesFundingAmanda = "0x89C05531C057565383EC088B4C241C8B7C2420C70100000000C74104000000008844010883C0013D0001000075F28D910001000031DB8954240489C831D2891C2489CEEB32C704240100000031ED0FB648080FB61C2F8D2C198D5415000FB6D20FB66C160889EB88580883C001884C16083B44240474128B0C24394C24247EC58B2C2483042401EBC583C4085B5E5F5DC2100089DB5557565383EC088B5424248B44241C8B6C242085D28B188B48047E5B31D2895C2404892C248B5C240483C30181E3FF000000895C24040FB67418088B6C24048D0C0E0FB6C90FB67C080889FB885C280889F38D343781E6FF000000885C08080FB67430088B3C2489F3301C1783C2013B54242475B089EB891889480483C4085B5E5F5DC21000"

# # Find the position of the substring "89C0" in the given string
# position_of_substring = MagazinesFundingAmanda.find("89C0")

# # Calculate the length of the substring from the beginning to the first occurrence of "89C0"
# investigationschess = (position_of_substring - 3) // 2 if position_of_substring != -1 else 0

# print(investigationschess)


# # Given hexadecimal string
# hex_string = "89C05531C057565383EC088B4C241C8B7C2420C70100000000C74104000000008844010883C0013D0001000075F28D910001000031DB8954240489C831D2891C2489CEEB32C704240100000031ED0FB648080FB61C2F8D2C198D5415000FB6D20FB66C160889EB88580883C001884C16083B44240474128B0C24394C24247EC58B2C2483042401EBC583C4085B5E5F5DC2100089DB5557565383EC088B5424248B44241C8B6C242085D28B188B48047E5B31D2895C2404892C248B5C240483C30181E3FF000000895C24040FB67418088B6C24048D0C0E0FB6C90FB67C080889FB885C280889F38D343781E6FF000000885C08080FB67430088B3C2489F3301C1783C2013B54242475B089EB891889480483C4085B5E5F5DC21000"

# # Convert hexadecimal string to binary data
# binary_data = bytes.fromhex(hex_string)

# # Display binary data (for testing purposes)
# print(binary_data)

