import elevhandler


looping = True

skola = elevhandler.ElevHandler()

skola.print_meny


while looping:
    val = skola.print_meny()

    if (val == "1"):
        print("...")
        print("lista elever")

    elif (val == "2"):
        namn=input("mata in namnet:   ")
        utb = input("mata in utbildning")
        tel = input("mata in telefonnummer")


        skola.add_elev(namn, utb, tel)
        

    elif (val == "3"):
        print ("ta bort elev")

    


    else :
        break