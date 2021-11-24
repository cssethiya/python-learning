secret_number = 5
guss= ""

guess_count=0
guess_limit=4
out_of_limit = False

while guss!= secret_number and not (out_of_limit):
    if guess_count<guess_limit:
        guss= int(input("Enter the number: "))
        guess_count+=1
    else:
        out_of_limit="True"

if out_of_limit:
    print("Your guss limmit is over ")
    print("Better luck next time: You Losse")

else:
    print("Congratulations: You Won")


