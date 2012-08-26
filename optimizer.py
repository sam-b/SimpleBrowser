def optimize(exp): 
    etype = exp[0] 
    if etype == "binop":
        a = optimize(exp[1])
        op = exp[2]
        b = optimize(exp[3])
        if a[0]=="number" and b[0]=="number":
            if op=="+":
                return ("number",a[1] +b[1])
            if op=="-":
                return ("number",a[1] -b[1])
            if op=="*":
                return ("number",a[1] * b[1])
            if op=="/":
                return ("number",a[1] / b[1])
        return ("binop",a,op,b)
    # leave this expression un-optimized 
    return exp 