from utlis import model
import customtkinter as ctk

window = ctk.CTk()
window.title('Student Mark Predictor')


root = ctk.CTkFrame(window,height=500, width=400) 
root.pack(padx=2, pady=2)

# ====================================
#  User Interfaces
# ====================================
def click():
    user_input = student_mark_entry.get()
    score = model.Prediction(user_input)
    if score is not None:
        output_label.configure(
            text=f'Predicted Mark : {score:.2f}'
        )
    else:
        output_label.configure(
            text=f'Invalid Input'
        )


label1 = ctk.CTkLabel(root,padx=20,pady=20)
label1.grid()

student_mark = ctk.CTkLabel(label1, text='Study Hour ', 
                             font=('Arial', 18),
                             
                             corner_radius=5,
                             padx=20, pady=20,
                             width=150, height=150, 
                             )
student_mark.grid(row=0, column=0)

student_mark_entry = ctk.CTkEntry(label1,
                                  width=190, height=50, 
                                  corner_radius=5)

student_mark_entry.grid(row=0, column=1)



# ====================================
#  Prediction Interfaces
# ====================================

label2 = ctk.CTkLabel(root,padx=20,pady=20)
label2.grid()

output_label = ctk.CTkLabel(label2, text='Prediction Displays here!',
                            fg_color='blue',
                            font=('Arial', 20, 'bold'),
                            width=150, height=90, 
                            corner_radius=5)
output_label.grid(row=0, column=0)

prediction_button = ctk.CTkButton(label2, 
                                  text='Predict',font=('Arial', 18),
                                  width=150, height=50,
                                  corner_radius=5, command=click)
prediction_button.grid(row=0,column=1)

window.mainloop()