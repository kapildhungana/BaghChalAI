from re import L
import tkinter
import time
from PIL import Image, ImageTk
from game import Game

class Board:

    def __init__(self):
        window = tkinter.Tk()
        window.geometry("900x600")
        window.title("Baghchal")
        self.arr=[0]
        self.graph=[[[20,20],[135,20],[250,20],[365,20],[480,20]],[[20,135],[135,135],[250,135],[365,135],[480,135]],[[20,250],[135,250],[250,250],[365,250],[480,250]],[[20,365],[135,365],[250,365],[365,365],[480,365]],[[20,480],[135,480],[250,480],[365,480],[480,480]]]
        self.l1 = tkinter.Label(window,text="AI Baghchal", font=("Arial Bold",20)).place(x=150,y=20)
        self.canvas = tkinter.Canvas(window, width=500, height=500,bg="skyblue")
        self.canvas.place(x=20,y=60)
        game = Game()
        self.canvas.after(10,self.render(game.boardgrid))

        # while game.is_game_over() == False:
        #     game.make_a_move()
        #     print(game.boardgrid)
        #     self.canvas = tkinter.Canvas(window, width=500, height=500,bg="skyblue")
        #     self.canvas.place(x=20,y=60)
        #     self.canvas.after(10,self.render(game.boardgrid))
        #     game.switch_turn()



# label = tkinter.Label(window, text="\n\n\n\n\n       Welcome to AI Baghchal         \n\n\n\n\n").pack()

        # self.arr2=game.boardgrid


        
        window.mainloop()

# display = Frame(window)

# game = Game()

    def draww(self,arr3):
        self.canvas.after(1000,self.render(arr3))

    # def playy(self):
    #     game = Game()
    #     game.__init__()
        


    def draw(self,coordinates,type):
            img = Image.open(type)
            img = img.resize((40,40))
            self.arr[-1]=ImageTk.PhotoImage(img)
            self.canvas.create_image(coordinates[0],coordinates[1],image=self.arr[-1])
            self.arr.append(0)

            

    def render(self,arr):
        self.canvas.delete('all')
        self.canvas.create_line(20,20,480,480, fill="green", width=3)
        self.canvas.create_line(20,480,480,20, fill="green", width=3)
        self.canvas.create_line(19,20,482,20, fill="green", width=3)
        self.canvas.create_line(20,20,20,480, fill="green", width=3)
        self.canvas.create_line(19,480,482,480, fill="green", width=3)
        self.canvas.create_line(480,20,480,480, fill="green", width=3)
        self.canvas.create_line(20,250,480,250, fill="green", width=3)
        self.canvas.create_line(250,20,250,480, fill="green", width=3)
        self.canvas.create_line(20,135,480,135, fill="green", width=3)
        self.canvas.create_line(20,365,480,365, fill="green", width=3)
        self.canvas.create_line(135,20,135,480, fill="green", width=3)
        self.canvas.create_line(365,20,365,480, fill="green", width=3)
        self.canvas.create_line(20,250,250,20, fill="green", width=3)
        self.canvas.create_line(250,20,480,250, fill="green", width=3)
        self.canvas.create_line(480,250,250,480, fill="green", width=3)
        self.canvas.create_line(250,480,20,250, fill="green", width=3)
        for i in range(5):
            for j in range(5):
                if arr[i][j]=="T":
                    # button = tkinter.Button(window,text="Enter",command = lambda: window.after(1000,draw(graph[i][j],"tiger.png")))
                    # button.place(x=10,y=10)
                    self.draw(self.graph[i][j],"tiger.png")
                elif arr[i][j]=="G":
                    self.draw(self.graph[i][j],"goat.png")


# def play(self):
#         self.__init__()
        
#         while self.is_game_over() == False:
#             self.make_a_move()
#             self.switch_turn()
#         print(self.no_of_moves_made)
#         if self.winner == "Goat":
#             print("Goat has won the game")
#             self.no_of_goat_wins += 1
#         elif self.winner == "Tiger":
#             print("Tiger has won the game")
#             self.no_of_tiger_wins += 1
#         else:
#             print("The game ended in the draw")

#         print("No of goat wins :: ",self.no_of_goat_wins)
#         print("No of tiger wins :: ",self.no_of_tiger_wins)




# canvas.after(3000, render(arr2[2]))





#game.initi()
# while(not game.is_game_over()):
#     arr2=game.make_a_move()
#     game.switch_turn()
#     print(game.no_of_moves_made)
#     if game.winner == "Goat":
#         print("Goat has won the game")
#         game.no_of_goat_wins += 1
#     elif game.winner == "Tiger":
#         print("Tiger has won the game")
#         game.no_of_tiger_wins += 1
#     else:
#         print("The game ended in the draw")

#     print("No of goat wins :: ",game.no_of_goat_wins)
#     print("No of tiger wins :: ",game.no_of_tiger_wins)


    #graph=[[[20,20],[135,20],[250,20],[365,20],[480,20]],[[20,135],[135,135],[250,135],[365,135],[480,135]],[[20,250],[135,250],[250,250],[365,250],[480,250]],[[20,365],[135,365],[250,365],[365,365],[480,365]],[[20,480],[135,480],[250,480],[365,480],[480,480]]]

    



    # img = Image.open("tiger.png")
    # img = img.resize((40,40))
    # photoimage = ImageTk.PhotoImage(img)
    # img = canvas.create_image(150,150,image=photoimage)
    # arr=[0]
    # def display(event):
    #     arr[-1]=ImageTk.PhotoImage(img)
    #     img2 = canvas.create_image(event.x,event.y,image=arr[-1])
    #     arr.append(0)

    # canvas.bind('<Button-1>',display)

    # img = Image.open("tiger.png")
    # img = img.resize((40,40))
    # arr=[0]

    # arr=[0]

    

    # arr2=[['T','_','_','_','_'],['G','G','G','G','T'],['_','_','T','_','_'],['G','G','T','G','G'],['G','G','G','G','G']]
    

    # for i in range(5):
    #     for j in range(5):
    #         draw(graph[i][j],"tiger.png")

# time.sleep(4000)
# arr2=[['T','T','T','T','T'],['G','G','G','G','T'],['_','_','T','_','_'],['G','G','T','G','G'],['G','G','G','G','G']]













# img = Image.open("tiger.png")
# img = img.resize((40,40))
# img = ImageTk.PhotoImage(img)
# label = tkinter.Label(window,image=img)
# label.place(x=400,y=100)

board = Board()
