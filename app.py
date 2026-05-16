import tkinter
from utlis import model

root = tkinter.Tk()
root.title('Student Mark Predictor')

root.configure(
    bg='white'
)

frame = tkinter.Frame(root)
frame.pack()

# ====================================
#  User Interfaces
# ====================================
def click():
    user_input = student_mark_entry.get()
    score = model.Prediction(user_input)
    if score is not None:
        output_label.config(
            text=f'Predicted Mark : {score:.2f}'
        )
    else:
        output_label.config(
            text=f'Invalid Input'
        )


label_frame = tkinter.LabelFrame(frame, text='Enter Study hours:', padx=20,pady=20)
label_frame.grid(row=0, column=0)

student_mark = tkinter.Label(label_frame, text='Study Hour ', 
                             font=('Arial', 16),padx=20, pady=20, bd=5)
student_mark.grid(row=0, column=0)

student_mark_entry = tkinter.Entry(label_frame)
student_mark_entry.grid(row=0, column=1)

prediction_button = tkinter.Button(label_frame, text='Predict',font=('Arial', 12), command=click)
prediction_button.grid(row=1,column=1)

# ====================================
#  Prediction Interfaces
# ====================================
output_frame = tkinter.LabelFrame(frame, text='Predicted:', padx=20, pady=20)
output_frame.grid(row=1)

output_label = tkinter.Label(output_frame, text='Output Displays here!',font=('Arial', 16),)
output_label.grid(row=0)

root.mainloop()