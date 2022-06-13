import random

comp_wins = 0
player_wins= 0
def choose_opton():
    user_choice = input ("Choose Rock, Papper or Scissors: ")
    if user_choice in ["Rock", " rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in["Papper", "papper","p","P"]:
        user_choice  = "p"
    elif user_choice in [" scissors", "scissors", "s", "S"]:
        user_choice = "s"
    else:
        print (" wrong input, try again.")
        choose_option()
    return user_choice
    
    def computer_option() :
        comp_choice = random.randint(1,3)
        if comp_choice == 1:
            comp_choice = "r"
        elif comp_choice == 2:
            comp_choice = "p"
        else:
            comp_choice = "s"
        return comp_choice 

    while True:
        print("")
        user_choice = choose_option()
        comp_choice = computer_option()
        print("")

        if user_choice == "r":
            if comp_choice == "r":
                print(" you chose rock. the computer chose rock.  you tied.")
            elif comp_choice == "p":
                print(" you chose rock. the computer chose paper. you lose'")
                comp_wins += 1
            elif comp_choice == "s":
                print (" you chose rock. the computer chose scissors. you win.")
                player_wins+= 1
        elif user_choice == "p":
            if comp_choice == "r":
                print ("you chose paper. the computer chose rock. you win")
                player_wins += 1
            elif comp_Choice == "p":
                print(" you chose paper. the computer chose paper. you tied.")
            elif comp_choice == "s":
                print("you chose papper. the computer chose scissors. you lose.")
                comp_wins += 1
        elif use_choice == "s":
            if comp_choice == "r":
                print("you chose scissors. the computer chose rock. you lose.")
                comp_wins += 1
            elif comp_choice == "p":
                print ("you chose scissors. the computer chose paper. you win.")
                player_wins =+ 1
            elif comp_choice == "s":
                print (" you chose scissors. the computer chose scissors. you tied.")

        print("")
        print("player wins: "+ str(player_wins))
        print ("computer wins: " + str(comp_wins))
        print("")

        user_choice = input (" Do you want to play again? (y/n")
        if user_choice in [ "Y", "y","yes", "Yes"]:
            pass
        elif user_choice in ["N","n","no","No"]:
            break
        else:
            break
                
        
                
        
        
        
