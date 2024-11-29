# ---------------------------- 1 str_counter_added_dic-------------------------------
# def str_counter(strs):
#     dic = {}
#     for x in strs:
#         dic[len(x)] = x
#     print(dic)
# str_counter(["shaftoli", "olma", "nok"])

# ------------------------------ 2 add_2list_dict------------------------------

# list_1 = ["a", "b", "c"] 
# list_2 = [1, 2, 3]
# dict = {}
# def merge_list(l1,l2):
#     c=0
#     for x in l1:
#         dict[x] = l2[c]
#         c+=1
#     print(dict)

# merge_list(list_1,list_2)

# ------------------------------------ 3 miniPhone --------------------------

# contacts = {"Nodir":"+998918602711", "Laziz":"+998908002534"}

# def miniTel_function(addK,addI):
#     contacts[addK] = addI
#     return print(contacts)

# def update(info):
#     contacts.update(info)
#     return print(contacts)

# def delete(info):
#     del contacts[info]
#     return print(contacts)

# def search(info):
#     return print(contacts.get(info))

# data = int(input(f"""
#     Bu mini telefon dasturi
#     Bu esa sizning contactlaringiz: "Nodir: +998918602711", "Laziz: 998908002534"
#     Siz bajara oladigan ishlar:
#        1) kontakt qoshish - "Ism" "Nomer", 2) Bor kontakni ozgartirish - "Kontakt" "Nomer", 3) ochirish - "ochirish kerak bolgan Kontankt" ,
#             4) Qidiruv - "kontakt nomi".
#     bajarmoqchi bolgan ishingizni raqamini kiriting: > 
# """))

# while data != "stop":
#     if data == 1:
#         datak = input(" kontakt qoshish - 'Ism': > ")
#         datav = input(" kontakt qoshish - 'Nomer': > ")
#         miniTel_function(datak, datav)
#         data = int(input(f"""
#     Bu mini telefon dasturi
#     Bu esa sizning contactlaringiz: "Nodir: +998918602711", "Laziz: 998908002534"
#     Siz bajara oladigan ishlar:
#        1) kontakt qoshish - "Ism" "Nomer", 2) Bor kontakni ozgartirish - "Kontakt" "Nomer", 3) ochirish - "ochirish kerak bolgan Kontankt" ,
#             4) Qidiruv - "kontakt nomi".
#     bajarmoqchi bolgan ishingizni raqamini kiriting: > 
# """))
#     elif data == 2:
#         datak = str(input("Bor kontakni ozgartirish - 'Kontakt nomi': > "))
#         if  datak not in contacts.keys():
#             print("siz kontaktda yoq bolgan ism kiritingiz!")
#         else: 
#             datav = input("Bor kontakni ozgartirish - 'nomer': > ")
#             update([[datak,datav]])
#             data = int(input(f"""
#     Bu mini telefon dasturi
#     Bu esa sizning contactlaringiz: "Nodir: +998918602711", "Laziz: 998908002534"
#     Siz bajara oladigan ishlar:
#        1) kontakt qoshish - "Ism" "Nomer", 2) Bor kontakni ozgartirish - "Kontakt" "Nomer", 3) ochirish - "ochirish kerak bolgan Kontankt" ,
#             4) Qidiruv - "kontakt nomi".
#     bajarmoqchi bolgan ishingizni raqamini kiriting: > 
# """))
#     elif data == 3:
#         datak = input("ochirish - 'ochirish kerak bolgan Kontankt': > ")
#         if  datak not in contacts.keys():
#             print("siz kontaktda yoq bolgan ism kiritingiz!")
#         else:
#             delete(datak)
#             data = int(input(f"""
#     Bu mini telefon dasturi
#     Bu esa sizning contactlaringiz: "Nodir: +998918602711", "Laziz: 998908002534"
#     Siz bajara oladigan ishlar:
#        1) kontakt qoshish - "Ism" "Nomer", 2) Bor kontakni ozgartirish - "Kontakt" "Nomer", 3) ochirish - "ochirish kerak bolgan Kontankt" ,
#             4) Qidiruv - "kontakt nomi".
#     bajarmoqchi bolgan ishingizni raqamini kiriting: > 
# """))
#     elif data == 4:
#         datak = input("Qidiruv - 'kontakt nomi': > ")
#         if  datak not in contacts.keys():
#             print("siz kontaktda yoq bolgan ism kiritingiz!")
#         else: 
#             search(datak) 
#             data = int(input(f"""
#     Bu mini telefon dasturi
#     Bu esa sizning contactlaringiz: "Nodir: +998918602711", "Laziz: 998908002534"
#     Siz bajara oladigan ishlar:
#        1) kontakt qoshish - "Ism" "Nomer", 2) Bor kontakni ozgartirish - "Kontakt" "Nomer", 3) ochirish - "ochirish kerak bolgan Kontankt" ,
#             4) Qidiruv - "kontakt nomi".
#     bajarmoqchi bolgan ishingizni raqamini kiriting: > 
# """))
            

# ----------------------------------- 4 counter_dict(nums) -----------------------

# dict = {}
# def counter_dict(nums):
#    for x in nums:
#         c = nums.count(x)
#         dict[x] = c
#         print(dict)
#         # return dict
# print(counter_dict([2,1,1,1]))



# -------------------------- 5 ------------------------------


# def max_ball_students(talabalar):
#     sort = sorted(talabalar.items(), key=lambda item: item[1], reverse=True)
#     print(sort[:2])
# max_ball_students({"Akmal": 64, "Tohir": 55, "Nodir": 76, "Zafar": 80}) 