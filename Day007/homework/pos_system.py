




def pos_system(num,curr_pos,target_pos):

    # გადავიყვანთ ყველა შესაძლო შემომავალ პოზიციური სისტემის რიცხვს 10ობით სისტემაში, რადგან უფრო მარტივად მოხდეს კონვერტაცია 10ობითიდან შემდეგ უკვე სხვადასხვა პოზიციურ სისტემაში,ამაში დაგვჭირდა int() ფუნქცია რომელსაც გადავეცით არგუმენტად ორი მნიშვნელობა
    # პირველი: შემოსული რიცხვი რომელიც უნდა გადაიქცეს 10ობით სისტემაში(თუ 10ობითია საწყისი რიცხვი მაშინ არაფერი არ შეიცვლება)
    # მეორე:მივუთითებთ უკვე რომელი პოზიციური სისტემიდან გვინდა გადაქცევა 10ობითში 

    number = 0

    for i in range(len(num)-1,-1,-1):
        number += int(num[i]) * curr_pos ** i
    # num = int(num,current_pos)
    number = int(str(number)[::-1])

    # აქ მოწმდება თუ ის პოზიცია რომელშიც გვსურს გადაქცევა არის 10ობითი მაშინ პირდაპირ დავაბრუნებთ კონკრეტულ რიცხვს, რომელიც უკვე გადაქცეულია ზემოთ მოცემული კოდის ხაზის მიხედვით 10ობითში
    if target_pos == 10:
        return number
    

    #აქ მოცემულია 16 ობითი სისტემის რიცხვები მაგრამ ერთი პოზიციიდან მეორეში გადასაყვანად გამოვიყენებთ ქვევით მოცემულ digits ცვლადს რადგან აქ შენახულია ყველა შესაძლო ციფრი და ასო
    digits = "0123456789ABCDEF"

    # ქვემოთ მოცემულ res ცვლადში შევინახავთ უკვე საბოლოო მნიშვნელობას
    res = ""

    # სანამ შემოსული რიცხვი მეტი იქნება 0 ზე გაეშვება , ქვევით მოცემულ while ციკლში გაშვებული ოპერაციები ხოლო თუ უკვე შემოსული რიცხვის განახლებული ვერსია იქნება 0 მაშინ while ციკლი გაჩერდება და დაბრუნდება უკვე საბოლოო მნიშვნელობა
    while number > 0:
        remainder = number % target_pos
        res += digits[remainder] 
        number = number // target_pos
    return res if res else "0"



num = input("Enter the number: ")
curr_pos = int(input("Enter the current Position: "))
target_pos = int(input("Enter the target position: "))


print(pos_system(num,curr_pos,target_pos))
