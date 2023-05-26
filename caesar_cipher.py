import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def ceaser(text,shift,direction):
    msg=''
    if direction=='decode':
        shift*=-1
    for i in text:
        if i in alphabet:
            pos=alphabet.index(i)
            new_index=pos+shift
            new_index%=26
            msg += alphabet[new_index]
        else:
            msg+=i    
    print(f"Here's the {direction}d result: {msg}") 

print(art.logo)
repeat='yes'
while repeat=="yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(text=text,shift=shift,direction=direction)
    repeat=input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
print("Goodbye.")