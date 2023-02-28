ANSWER = "=" #symbol for wanted answer variable
UNKNOWN = "?" #symbol for unknown variable

if __name__ == "__main__":
    print("Inputs should be taken in the form 'suvat(S,U,V,A,T)'")
    print("For known values input as a float or integer")
    print("For the desired answer input '"+ str(ANSWER)+ "' as a string")
    print("For an unknown term input '" + str(UNKNOWN)+"' as a string")

def suvat(s,u,v,a,t):
    #---Check number of string inputs---
    inputs = [s,u,v,a,t]
    count = inputs.count(ANSWER)
    if count != 1:
        return "You must input exactly one variable to be calcualated"
        #return breaks function so future code wont run'
    count = inputs.count(UNKNOWN)
    if count > 1:
        return "There can be no more than one unknown variable"


    #---Decide on appropriate formula---
    if s == ANSWER:
        if u == UNKNOWN:
            print("Use the formula: s=vt-1/2*at^2")
            print("s=("+str(v)+"*"+str(t)+")-(1/2*"+str(a)+"*"+str(t)+"^2)")
            print("s="+str((v*t)-(0.5*a*(t**2))))
        elif v == UNKNOWN:
            print("Use the formula: s=ut+1/2*at^2")
            print("s=("+str(u)+"*"+str(t)+")+(1/2*"+str(a)+"*"+str(t)+"^2)")
            print("s="+str((u*t)+(0.5*a*(t**2))))
        elif a == UNKNOWN:
            print("Use the formula: s=1/2(u+v)t")
            print("s=1/2*("+str(u)+"+"+str(v)+")*"+str(t))
            print("s="+str(0.5*(u+v)*t))
        elif t == UNKNOWN:
            print("Use the formula: s=v^2-u^2/2a")
            print("s="+str(v)+"^2-"+str(u)+"^2/2*"+str(a))
            print("s="+str(((v**2)-(u**2))/(2*a)))
        else:#no unknowns
            print("Any of the following formula would work:")
            print("s=vt-1/2*at^2")
            print("s=ut+1/2*at^2")
            print("s=1/2(u+v)t")
            print("s=v^2-u^2/2a")
            print("s="+str(0.5*(u+v)*t))#use formula with least computation

                  
    elif u == ANSWER:
        if s == UNKNOWN:
            print("Use the formula: u=v-at")
            print("u="+str(v)+"-"+str(a)+"*"+str(t))
            print("u="+str(v-(a*t)))
        elif v == UNKNOWN:
            print("Use the formula: u=(s-(1/2*a*t^2))/t")
            print("u=("+str(s)+"-(1/2*"+str(a)+"*"+str(t)+"^2))/"+str(t))
            print("u="+str((s-(0.5*a*(t**2)))/t))
        elif a == UNKNOWN:
            print("Use the formula: u=(2s/t)-v")
            print("u=(2*"+str(s)+"/"+str(t)+")-"+str(v))
            print("u="+str(((2*s)/t)-v))
        elif t == UNKNOWN:
            print("Use the formula: u=(v^2-2as)^1/2")
            print("u=("+str(v)+"^2-2*"+str(a)+"*"+str(s)+")^1/2")
            print("u="+str(((v**2)-2*a*s)**0.5))
        else:#no unknowns
            print("Any of the following formula would work:")
            print("u=v-at")
            print("u=s-(1/2*a*t^2)/t")
            print("u=(2s/t)-v")
            print("u=(v^2-2as)^1/2")
            print("u="+str(v-(a*t)))#use formula with least computation

        
    elif v == ANSWER:
        if s == UNKNOWN:
            print("Use the formula: v=u+at")
            print("v="+str(u)+"+"+str(a)+"*"+str(t))
            print("v="+str(u+(a*t)))
        elif u == UNKNOWN:
            print("Use the formula: v=(s+(1/2*a*t^2))/t")
            print("v=("+str(s)+"+(1/2*"+str(a)+"*"+str(t)+"^2))/"+str(t))
            print("u="+str((s+(0.5*a*(t**2)))/t))
        elif a == UNKNOWN:
            print("Use the formula: v=(2s/t)-u")
            print("v=(2*"+str(s)+"/"+str(t)+")-"+str(u))
            print("v="+str(((2*s)/t)-u))
        elif t == UNKNOWN:
            print("Use the formula: v=(u^2+2as)^1/2")
            print("v=("+str(u)+"^2+2*"+str(a)+"*"+str(s)+")^1/2")
            print("v="+str(((u**2)+2*a*s)**0.5))
        else:#no unknowns
            print("Any of the following formula would work:")
            print("v=u+at")
            print("v=(s+(1/2*a*t^2))/t")
            print("v=(2s/t)-u")
            print("v=(u^2+2as)^1/2")
            print("v="+str(u+(a*t)))#use formula with least computation
            
  
    elif a == ANSWER:
        if s == UNKNOWN:
            print("Use the formula: a=(v-u)/t")
            print("a=("+str(v)+"-"+str(u)+")/"+str(t))
            print("a="+str((v-u)/t))
        elif u == UNKNOWN:
            print("Use the formula: a=(2(vt-s))/t^2")
            print("a=(2("+str(v)+"*"+str(t)+"-"+str(s)+"))/"+str(t)+"^2")
            print("a="+str((2*((v*t)-s))/t**2))
        elif v == UNKNOWN:
            print("Use the formula: a=(2(s-ut))/t^2")
            print("a=(2("+str(s)+"-"+str(u)+"*"+str(t)+"))/"+str(t)+"^2")
            print("a="+str((2*(s-(u*t)))/t**2))
        elif t == UNKNOWN:
            print("Use the formula: a=v^2-u^2/2s")
            print("a="+str(v)+"^2-"+str(u)+"^2/2*"+str(s))
            print("a="+str(((v**2)-(u**2))/(2*s)))
        else:#no unknowns
            print("Any of the following formula would work:")
            print("a=(v-u)/t")
            print("a=(2(vt-s))/t^2")
            print("a=(2(s-ut))/t^2")
            print("a=v^2-u^2/2s")
            print("a="+str((v-u)/t))#use formula with least computation

    elif t == ANSWER:
        if s == UNKNOWN:
            print("Use the formula: t=(v-u)/a")
            print("t=("+str(v)+"-"+str(u)+")/"+str(a))
            print("t="+str((v-u)/a))
        elif u == UNKNOWN:
            print("Use the formula: t=(((v^2-2as)^1/2)-v)/-a")
            print("t=((("+str(v)+"^2-2*"+str(a)+"*"+str(s)+")^1/2)-"+str(v)+")/"+str(-a))
            print("t="+str(((((v**2)-(2*a*s))**0.5)-v)/-a))
        elif v == UNKNOWN:
            print("Use the formula: t=(((u^2+2as)^1/2)-u)/a")
            print("t=((("+str(u)+"^2+2*"+str(a)+"*"+str(s)+")^1/2)-"+str(u)+")/"+str(a))
            print("t="+str(((((u**2)+(2*a*s))**0.5)-u)/a))
        elif a == UNKNOWN:
            print("Use the formula: t=2s/u+v")
            print("t=2*"+str(s)+"/"+str(u)+"+"+str(v))
            print("t="+str((2*s)/(u+v)))
        else:#no unknowns
            print("Any of the following formula would work:")
            print("t=(v-u)/a")
            print("t=(((v^2-2as)^1/2)-v)/-a")
            print("t=(((u^2+2as)^1/2)-u)/a")
            print("t=2s/u+v")            
            print("t="+str((v-u)/a))#use formula with least computation
