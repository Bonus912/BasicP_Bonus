# haverice = True
# havespoon = False
# havehand = True

# if haverice:
#     if havespoon:
#         print("กินข้าว")
#     elif havehand:
#         print("กินข้าวเหนียว")

# score = int(input("Enter your score"))
    
# if 100 > score >= 80:
#     print(" A ")
# if 80 > score >= 70:
#     print(" B ")
# if 70 > score >= 60:
#     print(" C ")
# if 60 > score >= 50:
#     print(" D")

# score = int(input("Enter your score"))

# if score >= 0:
#     if score <= 100:
#         if score >= 80:
#             print(" A ")
#         if score >= 70:
#             if score < 80:
#                 print(" B ")
#         if score >= 60:
#             if score < 70:
#                 print(" C ")
#         if score >= 50:
#             if score < 60:
#                 print(" D ")
#         if score < 50:
#             print(" F ")

# for i in range(5):
#     print("สวัสดี")

# for i in range(8):
#     print("สวัสดี")

# for i in range(1,5):
#     print(i)

# for i in range(1,10,2):
#     print(i)

# i = 0
# while i < 5:
#     print("สวัสดี")
#     i = i + 1

# i = 0
# while i < 8:
#     print("สวัสดี")
#     i = i + 1

# i = 0
# while i < 5:
#     print(i)
#     i = i + 1


# while True:
#     choice = int(input("กรอก 1 เพื่อบวกเลข, กรอก 2 เพื่อออก"))

#     if choice == 1:
#         num = int(input("จำนวนเลขที่ต้องการจะบวก:"))
#         sumation = 0

#         for i in range(num):
#             num1 = int(input("กรอกเลข:"))
#             sumation = sumation + num1
        
#         print("ผลลัพท์", sumation)

#     if choice == 2:
#         print("บาย บาย")
#         break

monster = 50
sword = 20
knife = 10
wood = 5

while True:
    choice = int(input("กรอก 1 เพื่อต่อสู้กับมอนเตอร์, กรอก 2 เพื่อออก "))


    if choice == 1:
        print("เลือดมอนเตอร์; 50")
        print("อาวุธ 1.ดาบ(20) 2.มีด(10) 3.ไม้(5)")
        num = int(input("จำนวนครั้งที่จะตีมอนเตอร์ "))

        for i in range(num):
            num1 = int(input("เลือกอาวุธ 1.ดาบ(20) 2.มีด(10) 3.ไม้(5) "))
            if num1 == 1:
                monster = monster - sword
            if num1 == 2:
                monster = monster - knife
            if num1 == 3:
                monster = monster - wood
            if monster < 0:
                monster = 20
                print("มอนเตอร์ยังไม่ตาย")
            print("เลือดมอนเตอร์เหลือ " , monster)
            if monster == 0:
                print("คุณชนะ")
                break
        break


    elif choice == 2:
        print("บาย")        
        break