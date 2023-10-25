from tkinter import *

##### Assign Values for fonts and colors #####
CLR = "lightblue"
CLR2 = "#25265E"
WHITE = "#FFFFFF"
ON_CLR = "#F8FAFF"

DFFONT = ("Arial",20)
DFONT = ("Arial", 24, "bold")
SFONT = ("Times New Roman", 16, "italic")
BFONT = ("Times New Roman", 45, "bold")

#### Create a class called calculator #####
class calculator:
    
    ###### the atTributes of the class calculator ######
    def __init__(self):
        ##### Root Properties ######
        self.root = Tk()
        self.root.geometry("350x660")
        self.root.resizable(1,0)
        self.root.title("calculator_App")
        
        self.tot_exp = "" 
        self.inp_exp = ""
        self.frame_disp = self.crt_disp_frme()
        
        self.tot_lab, self.label = self.crt_disp_labei()
        self.digits = {
            7: (1,1), 8:(1,2), 9:(1,3),
            4: (2,1), 5:(2,2), 6:(2,3),
            1: (3,1), 2:(3,2), 3:(3,3),
            0: (4,2), '.':(4,1)
        }
        self.operations = {"/": "\u00F7", "*":"\u00D7", "-":"-", "+":"+"}
        self.btn_frame = self.crt_btn1_frme()
        
        self.btn_frame.rowconfigure(0, weight=0)
        for x in range(1,5):
            self.btn_frame.rowconfigure(x,weight=1)
            self.btn_frame.columnconfigure(x,weight=1)
        self.crt_dgt_btns()
        self.create_optr_bttns()
        self.crt_spc_btns()
        self.bind_keys()
    def bind_keys(self):
        self.root.bind("<Return>", lambda event: self.evaluate())
        for keys in self.digits:
            self.root.bind(str(keys), lambda event,digit=keys:self.add_to_exp(digit))
        for keys in self.operations:
            self.root.bind(keys, lambda event, optr=keys: self.append_optr(optr))
            
    def crt_spc_btns(self):
        self.crt_clr_btn()
        self.equal_bttn()
        self.sqr_btn()
        self.sqrt()
        
    
    ########## creating the Display parts of a calculator #######
    def crt_disp_labei(self):
        tot_lab = Label(self.frame_disp, text=self.tot_exp, anchor=E,
                        bg=CLR, fg= CLR2, font=SFONT)
        tot_lab.pack(expand=True, fill="both")
        
        lab1 = Label(self.frame_disp, text=self.inp_exp, anchor=E,
                        bg=CLR, fg= CLR2, font=BFONT)
        lab1.pack(expand=True, fill="both")
        return tot_lab, lab1
        
    
    ####### Display frame #########    
    def crt_disp_frme(self):
        frme = Frame(self.root,height=300,bg=CLR)
        frme.pack(expand=True, fill="both")
        return frme
    ##### FDislaying our values input ########
    def add_to_exp(self, value):
        self.inp_exp += str(value)
        self.update_lab()
    
    ########### Digits Buttons ##########
    def crt_dgt_btns(self):
        for digit, grid_value in self.digits.items():
            bttns = Button(self.btn_frame, text=str(digit),bg=WHITE,fg=CLR2,font=DFONT,
                           borderwidth=0, command=lambda x=digit:self.add_to_exp(x))
            bttns.grid(row=grid_value[0], column=grid_value[1],sticky=NSEW)
    
    def append_optr(self, optr):
        self.inp_exp += optr
        self.tot_exp += self.inp_exp
        self.inp_exp = ""
        self.update_tot_label()
        self.update_lab()

    ####### operations buttons #######
    def create_optr_bttns(self):
        i =0
        for optr,symbol in self.operations.items():
            bttns1 = Button(self.btn_frame, text=symbol,bg=ON_CLR,fg=CLR2,font=DFFONT,
                           borderwidth=0, command=lambda x=optr: self.append_optr(x))
            bttns1.grid(row=i,column=4, sticky=NSEW)
            i += 1
    
    ###### Clear button and functionality #######
    def clear(self):
        self.inp_exp = ""
        self.tot_exp = ""
        self.update_lab()
        self.update_tot_label()
            
    def crt_clr_btn(self):
        bttns = Button(self.btn_frame, text="C",bg="Royalblue",fg=CLR2,font=DFFONT,
                           borderwidth=0, command=self.clear)
        bttns.grid(row=0,column=1, sticky=NSEW)
    
    def square(self):
        self.inp_exp = str(eval(f"{self.inp_exp}**2"))
        self.update_lab()
    
    def sqr_btn(self):
        bttns = Button(self.btn_frame, text="x\u00b2",bg="Royalblue",fg=CLR2,font=DFFONT,
                           borderwidth=0, command=self.square)
        bttns.grid(row=0,column=2, sticky=NSEW)
    
    def square_root(self):
        self.inp_exp = str(eval(f"{self.inp_exp}**0.5"))
        self.update_lab()
    
    def sqrt(self):
        bttns = Button(self.btn_frame, text="x\u221ax",bg="Royalblue",fg=CLR2,font=DFFONT,
                           borderwidth=0, command=self.square_root)
        bttns.grid(row=0,column=3, sticky=NSEW)
    
    def evaluate(self):
        self.tot_exp += self.inp_exp
        self.update_tot_label()
        try:
            
            self.inp_exp = str(eval(self.tot_exp))
            self.tot_exp = ""
        except:
            self.inp_exp = "Error"
        finally:    
            self.update_lab()
             
    def equal_bttn(self):
        bttns = Button(self.btn_frame, text="=",bg="Green",fg=CLR2,font=DFFONT,
                           borderwidth=0, command=self.evaluate)
        bttns.grid(row=4,column=3, columnspan=3, sticky=NSEW)   
    
    ##### Button Frame #######    
    def crt_btn1_frme(self):
        frme = Frame(self.root)
        frme.pack(expand=True, fill="both")
        return frme
    
    def update_tot_label(self):
        expression = self.tot_exp
        for optr, symbol in self.operations.items():
            expression = expression.replace(optr, f" {symbol}")
        self.tot_lab.config(text=expression)
        
    def update_lab(self):
        self.label.config(text=self.inp_exp[:11])
                
    def run(self):
        self.root.mainloop()
        
 ##### this obj runs the gui ######       
if __name__ == "__main__":
   calc = calculator()
   calc.run() 