Special_charecters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
def has_uppercase(password):
   for char in password:
       if char.isupper():
           return True
   return False

def has_lowercase(password):
    for char in password:
        if char.islower():
            return True
    return False

def has_num(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def has_special_character(password):
    for char in password:
        if char in Special_charecters:
            return True
    return False
def check_password_strength(password):
    score=0
    tip=[]

    if len(password)>= 8 and len(password) <= 12:
        score+=1
    else:
        tip.append("Noch startker:mindistens 12 Zeichen.")
        
    if len(password) >=12:
        score+=1
    else:
        tip.append("Noch staerker: mindestens 12 Zeichen.")
    if has_uppercase(password):
        score+=1
    else:
        tip.append("Fuege mindestens einen Grossbuchstaben hinzu")
    if has_lowercase(password):
        score+=1
    else:
        tip.append("Fuege mindestens einen Kleinbuchstaben hinzu")
    if has_num(password):
        score+=1
    else:
        tip.append("Fuege mindestens eine Zahl hinzu")
    if has_special_character(password):
        score+=1
    else:
        tip.append("Fuege mindestens ein Sonderzeichen hinzu")
 
    return score, tip
def Score_check(score):
    if score <= 2:
        return "Schwach"
    elif score <= 4:
        return "Mittel"
    else:
        return "Stark"
print("Willkommen zum Passwort-Checker!")
print("Bitte geben Sie Ihr Passwort ein:")
user_password = input()
score, tips = check_password_strength(user_password)
print("Stärke:", Score_check(score))
for tip in tips:
    print(tip)
