import tkinter
from tkinter import StringVar


def calculate():
  try:
    str_h = entry_height.get()
    str_w = entry_weight.get()
    if str_h == "" or str_w == "":
      msg_result.set("Please enter both height and weight")
      return
    h = int(str_h)
    w = int(str_w)
    bmi = w / (h / 100) ** 2
    if bmi < 16:
      msg_result.set(f"Your BMI is {bmi:.2f} and you are severely underweight")
    elif bmi <= 18.4:
      msg_result.set(f"Your BMI is {bmi:.2f} and you are underweight")
    elif bmi <= 24.9:
      msg_result.set(f"Your BMI is {bmi:.2f} and you are normal")
    elif bmi <= 29.9:
      msg_result.set(f"Your BMI is {bmi:.2f} and you are overweight")
    elif bmi <= 34.9:
      msg_result.set(f"Your BMI is {bmi:.2f} and you are moderately obese")
    elif bmi <= 39.9:
      msg_result.set(f"Your BMI is {bmi:.2f} and you are severely obese")
    else:
      msg_result.set(f"Your BMI is {bmi:.2f} and you are morbidly obese")
  except:
    msg_result.set("Please enter integer values for height and weight")


root = tkinter.Tk()
root.title("BMI Calculator")
root.geometry("400x200")
root.config(padx=5, pady=5)
lbl_weight = tkinter.Label(root, text="Enter your weight (kg) ")
lbl_weight.pack(padx=5, pady=5)
entry_weight = tkinter.Entry(root)
entry_weight.pack(padx=5, pady=5)
lbl_height = tkinter.Label(root, text="Enter your height (cm) ")
lbl_height.pack(padx=5, pady=5)
entry_height = tkinter.Entry(root)
entry_height.pack(padx=5, pady=5)
btn_calc = tkinter.Button(root, text="Calculate", command=calculate)
btn_calc.pack(padx=5, pady=5)
msg_result = StringVar()
lbl_result = tkinter.Label(root, textvariable=msg_result)
lbl_result.pack(padx=5, pady=5)


root.mainloop()