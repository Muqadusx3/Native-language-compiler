

def int_1(code):
    if(code.startswith("je")):
        start_index = code.find("je") + len("je")
        end_index = code.find("aykarie")

        condition = code[start_index:end_index]
        start_index = code.find("aykarie") + len("aykarie")
        end_index = code.find("nite")
        t_s = code[start_index:end_index]
        start_index = code.find("nite") + len("nite")
        f_s = code[start_index:]

        c = '''
        if {condition}:
          print({t_s})
        else:
          {f_s}
        '''

        exec(c)
        generate_intermediate_code(condition, t_s, f_s)
        
# Example usage:
    elif(code.startswith("jando")):
        start_index = code.find("jando") + len("jando")
        end_index = code.find("aykarie")
        generate_intermediate_code(condition, t_s, f_s)
        condition = code[start_index:end_index]
 
        start_index = code.find("aykarie") + len("nite")
        f_s = code[start_index:]

        def generate_intermediate_code(condition,f_s):
           c='''while {condition}:
              print({f_s})
             '''
           exec(c)
           
        generate_intermediate_code(condition,f_s)  
    elif(code.startswith("chaldawanj")):
        start_index = code.find("chaldawanj") + len("chaldawanj")
        end_index = code.find("nu")
        
        condition = code[start_index:end_index]
      
        start_index = code.find("aykarie") + len("nite")
        f_s = code[start_index:]

        def generate_intermediate_code(condition,f_s):
           c='''for {condition} in range(10):
              print({f_s})
             '''
           exec(c)
           
        generate_intermediate_code(condition,f_s)  
    elif(code.startswith("das")):
      start_index = code.find("das") + len("das")
      st = code[start_index:]
      def generate_intermediate_code(st):
           c="print("+st+")"
           c1=st
           exec(c)
      generate_intermediate_code(st)
      return st
    else:
      exec(code)
      
