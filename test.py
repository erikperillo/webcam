import oarg

oi = oarg.Oarg(tuple,"-o",(9,3),"tub",0)

oarg.parse()

print oi.getVal()
