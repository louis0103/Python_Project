#   Python 程式設計 HW_2
z=characterUsed="print({*z})"
exec(z)
#{'n','*','i','r','z','}','(',')','t','{','p'}

x="hello"
d={'name':'louis'}; d.clear();
z="x+x"
exec(z); print(d);
#{'h':{...}}
exec(characterUsed)
#{'d','*',']','[','5','x',='}

z="print(("+z+"))"
exec("print(("+z+"))")
# True
print(eval(z))
#True
exec(characterUsed)
# {'d',']','h','[','i','s','',""}
