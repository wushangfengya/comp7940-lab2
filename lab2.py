import json
import requests
site="https://api.npoint.io/2b57052af2060e84dc86"
r = requests.get(site)
print(r.json())
text = r.json()['users']
for i in text:
    print("parse " + str(i))
def convert_number(elements):
    return [int(e) for e in elements[1:]]
y = convert_number(text[0])
print("y")
print(y)
def replace_number(number_list, being_replace, to_replace):
    return [to_replace if number == being_replace else number for number in number_list]
z = replace_number(number_list = y, being_replace = 1, to_replace =10)
print("z")
print(z)
sum = 0
for i in z:
    sum = sum + i
    print("sum = " + str(sum) + "; i =" + str(i))
print ("Total = " + str(sum))

