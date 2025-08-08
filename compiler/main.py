
import tkinter as tk
import call
import re
import int_
def remove_comments(code):
    code_without_comments = re.sub(r'(?m)^\s*#.*\n?', '', code)
    code_without_comments = re.sub(r'(?s)/\*.*?\*/', '', code_without_comments)
    return code_without_comments

    
def run_compiler():
    
    code = input_text.get("1.0", "end-1c")
    if (code.startswith("das")):
        st=int_.int_1(code)
        output_text.insert("end", "Valid")
        output_text.insert("end", int_.int_1(code))
    else:
    # Remove comments from code
     code_ = remove_comments(code)
    
     result, error, tokens, parser_list, stm= call.run('<stdin>', code)
    
     if error:
        output_text.delete("1.0", "end")
        output_text.insert("end", error.as_string())
     elif result:
        output_text.delete("1.0", "end")
        va=call.valid()
        print(va)
        if va:  
            output_text.insert("end", "Valid")
            output_text.insert("end", "")
            st=int_.int_1(code)
        else:
           output_text.insert("end", "Invalid")
           output_text.insert("end", f"Lexer Output:\n{tokens}\n\nParser Output:\n{'\n'.join(parser_list)}\n\nSTM Output:\n{stm}")
     

root = tk.Tk()
root.title("PUNJABI COMPILER")
# Heading
heading_label = tk.Label(root, text="PUNJABI COMPILER", font=("Cambria", 20), fg="blue")
heading_label.pack(pady=10)


# Input Space
input_frame = tk.Frame(root)
input_frame.pack(side=tk.TOP, padx=10, pady=10)

input_label = tk.Label(input_frame, text="Input:")
input_label.pack(anchor='w')

input_text = tk.Text(input_frame, height=10, width=60)
input_text.pack()

# Run Button
run_button = tk.Button(root, text="Run", command=run_compiler)
run_button.pack(anchor='center', pady=10)

# Output Space
output_frame = tk.Frame(root)
output_frame.pack(side=tk.BOTTOM, padx=10, pady=10)

output_label = tk.Label(output_frame, text="Output:")
output_label.pack(anchor='w')  # Set the side to LEFT

output_text = tk.Text(output_frame, height=10, width=60)
output_text.pack()

root.mainloop()

run_button = tk.Button(root, text="Run", command=run_compiler)
run_button.pack(side=tk.RIGHT, pady=10)
# Output Space
output_frame = tk.Frame(root)
output_frame.pack(side=tk.BOTTOM, padx=10, pady=10)

output_label = tk.Label(output_frame, text="Output:")
output_label.pack(anchor='w')  # Set the side to LEFT

output_text = tk.Text(output_frame, height=10, width=60)
output_text.pack()

# Run Button
root.mainloop()



