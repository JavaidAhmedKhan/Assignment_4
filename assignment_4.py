# Assigement 4

import re

txt = '''Please contact me at 0301-1234567 or 042-35678901 for further details.'''
new_txt = re.sub("-","",txt)
pattern = r"\d{11}"
result = re.findall(pattern, new_txt)
print(result)

# Assignment 2 - Validating Email address
var = '''Contact us at info@example.com or support@domain.pk for assistance.'''
pattern = r"\b[\w\.-]+@[\w]+\.+[\w]+"
var_result = re.findall(pattern,var)
print(var_result)

# Assignment 3 - Validating CNIC #
cnic = '''My CNIC is 12345-6789012-3 and another one is 34567-8901234-5.'''
pattern = r"\d{5}-\d{7}-\d{1}"
result = re.findall(pattern,cnic)
print(result)

# Assignment 4 - Identifing Urdu Word
text = '''یہ sentence میں کچھ English words بھی ہیں۔'''
pattern = r"[^A-z]+"
result = re.findall(pattern,text,re.UNICODE)
print(result)

# Assignment 5 - Identifing Dates

text = '''The event will take place on 15-08-2023 and 23-09-2023.'''
pattern = r"\d{2}-\d{2}-\d{4}"
result = re.findall(pattern, text)
print(result)

# Assignment 6 - Extracting URL

url = '''Visit http://www.example.pk or https://website.com.pk for more information.'''
pattern = r"\bh+[^\s]+"
result = re.findall(pattern, url)
print(result)

# Assignment 7 - Extracting Currency

text = '''The product costs PKR 1500, while the deluxe version is priced at Rs. 2500.'''
new_text = re.sub("Rs.","PKR",text)
pattern = r"\w{3} \d{4}"
result = re.findall(pattern, new_text)
print(result)

# Assignment 8 - Removing Punctuation
rp = '''کیا! آپ, یہاں؟'''
pattern = r"[\w]+"
result = re.findall(pattern,rp)
print(result)

# Assignment 9 - Extracting Cities Name

text = '''Text: Lahore, Karachi, Islamabad, and Peshawar are major cities of Pakistan.'''
pattern = r"(?![T])[A-Z][A-z]+\b[^.]"
result = re.findall(pattern,text)
print(result)





# Assignment 10 - Analyzing Vehicle Numbers

veh = '''Text: I saw a car with the number plate LEA-567 near the market.'''
pattern = r"\w{3}-\d{3}"
result = re.findall(pattern,veh)
print(result)