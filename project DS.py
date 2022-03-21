
print("\n------------------ Welcome to Data structure calculator ------------------")
print("\n      1.List " "\n      2.Tuple" "\n      3.Set " "\n      4.Dictionary\n")

ds=input("Enter any one Data Structure")
if ds=="1":
    lst=[]
    print("First create your List")
    L=int(input("Enter number of elements"))
    for ELE in range(L): 
        L_ele=int(input("Enter List element"))
        lst.append(L_ele)
    print(lst)
    Lstopn=int(input("Enter number of operation do you want to"))
    for op in range(Lstopn):
     print("---------\nList operations \n  1.Append \n  2.Pop \n  3.Update/concatenation \n  4.Sum \n  5.Min \n  6.Max \n  7.Pop \n  8.Len \n  9.Reverse \n  10.Find \n  11.Frequency \n  12.Insert \n  13.Extend \n  14.Remove \n  15.Count \n  16.Clear \n  17.Sort \n  ")
     Lstop=int(input("Enter operation do you want to"))      
     if Lstop==1:
        app=int(input("Enter ele to Append"))
        lst.append(app)
        print("List after append==>",lst)
     elif Lstop==2:
         pp=int(input("Enter ele to pop"))
         if pp in lst:
             lst.pop(pp)
             print("List after pop==>",lst)
         else:
             print("out of index pls enter valid index to pop")
     elif Lstop==3:
         nlst=[]
         NL=int(input("enter number of ele in the new list..."))
         for i in range(NL):
             nle=int(input("enter ele in the new list..."))
             nlst.append(nle)
         print("List after Update==>",lst+nlst)
     elif Lstop==4:
         print("sum of List==>",sum(lst))
     elif Lstop==5:
        print("min of List==>",min(lst))
     elif Lstop==6:
        print("max of List==>",max(lst))
     elif Lstop==7:
        lst.pop()
        print("List after pop==>",lst)
     elif Lstop==8:
        print("len of List==>",len(lst))
     elif Lstop==9:
         lst.reverse()
         print("Reverse  of List==>",lst)
     elif Lstop==10:
         find=int(input("Enter ele to Find"))
         if find in lst:
             lst.index(find)
             print(f"{find} is in the index of",lst)
         else:
             print(f"{find} is not in the list")
     elif Lstop==11:
         freq={}
         for i in lst:
             if i in freq:
                 freq[i]+=1
             else:
                 freq[i]=1
         print("Frequency of list is",freq)
     elif Lstop==12:
         upi=int(input("Enter index to Insert"))
         upe=int(input("Enter ele to Insert"))
         lst.insert(upi,upe)
         print("List after Insert==>",lst)
     elif Lstop==13:
         nlst=[]
         nl=int(input("enter number of ele in the new list..."))
         for i in range(nl):
                nle=int(input("enter ele in the new list..."))
                nlst.append(nle)
         lst.extend(nlst)
         print("List after extended",lst)
     elif Lstop==14:
         rele=int(input("enter number to remove in list..."))
         if rele in lst:
             print(f"List after remove {rele}",lst.remove(rele))
         else:
             print(f"{rele} is not in the List ")
     elif Lstop==15:
         lst.count()
         print(" The count of list is",lst)
     elif Lstop==16:
         lst.clear()
         print("List after cleared",lst)
     elif Lstop==17:
         lst.sort()
         print("List after sorted",lst)
     else:
        print("Enter the valid List operation")
        print("List operations \n  1.Append \n  2.Pop \n  3.Update/concatenation \n  4.Sum \n  5.Min \n  6.Max \n  7.Pop \n  8.Len \n  9.Reverse \n  10.Find \n  11.Frequency \n  12.Insert \n  13.Extend \n  14.Remove \n  15.Count \n  16.Clear \n  17.Sort \n  ")
        Lstop=int(input("Enter operation do you want to"))



elif ds=="2":
    lst=[]
    print("First create your Tuple")
    L=int(input("Enter number of elements"))
    for ELE in range(L): 
        L_ele=int(input("Enter List element"))
        lst.append(L_ele)
    tpl=tuple(lst)
    print(tpl)
    tplopn=int(input("Enter number of operation do you want to"))
    for op in range(tplopn):
     print("---------\nTuple operations \n  1.Append \n  2.Concatenation \n  3.Find \n  4.Count \n  5.sum \n  6.Len \n  7.Min \n  8.Max \n  9.Delete \n ")
     Tplop=int(input("Enter operation do you want to"))
     if Tplop==1:
         app=int(input("Enter ele to Append"))
         lst.append(app)
         tpl=tuple(lst)
         print("Tuple after append==>",tpl)
     elif Tplop==2:
         nlst=[]
         NL=int(input("enter number of ele in the new tuple..."))
         for i in range(NL):
             nle=int(input("enter ele in the new tuple..."))
             nlst.append(nle)
         ntpl=tuple(nlst)
         print("Tuple after Concatenation==>",tpl+ntpl)
     elif Tplop==3:
         find=int(input("Enter ele to Find"))
         if find in tpl:
             print(f"{find} is in the index of",tpl.index(find))
         else:
             print(f"{find} is not in the tuple")
     elif Tplop==4:
         print(" The count of tuple is",tpl.count(tpl))
     elif Tplop==5:
         print("sum of tuple==>",sum(tpl))
     elif Tplop==6:
         print("length of tuple==>",len(tpl))
     elif Tplop==7:
         print("min of tuple==>",min(tpl))
     elif Tplop==8:
         print("max of tuple==>",max(tpl))
     elif Tplop==9:
         del(tpl)
     else:
         print("Enter the valid tuple operation")
         print("---------\nTuple operations \n  1.Append \n  2.Concatenation \n  3.Find \n  4.Count \n  5.sum \n  6.Len \n  7.Min \n  8.Max \n  9.Delete \n ")
         Tplop=int(input("Enter operation do you want to"))
    sett=set(lst)
    print(sett)
    setopn=int(input("Enter number of operation do you want to"))
    for op in range(setopn):
        print("---------\nSet operations \n  1.Add \n  2.Update \n  3.Remove \n  4.Discard \n  5.pop \n  6.Clear \n  7.Copy \n  8.Delete \n  9.Union \n  10.Intersection \n  11.Difference \n  12.Is_disjoin \n  13.Is_subset \n  14.Is_superser \n  15.Difference_update \n ")
        setop=int(input("Enter operation do you want to"))
        if setop==1:
            add=int(input("Enter ele to Add"))
            sett.add(add)
            print(sett)
            nlst=[]
            NL=int(input("enter number of ele in the new set..."))
            for i in range(NL):
               nle=int(input("enter ele in the new set..."))
               nlst.append(nle)
            Nset=set(nlst)
            sett.update(Nset)
            print("Set after update==>",sett)
        elif setop==3:
            rmv=int(input("Enter ele to Remove"))
            if rmv in sett:
                sett.remove(rmv)
                print(f"Set after Remove {rmv} ==>",sett)
            else:
                print(f"{rmv} not found in set")
        elif setop==4:
            rmv=int(input("Enter ele to Remove"))
            sett.discard(rmv)
            print(f"Set after Discard {rmv} ==>",sett)
        elif setop==5:
            sett.pop()
            print(f"Set after pop {sett.pop()} ==>",sett)
        elif setop==6:
            print("Set after clear ==>",sett.clear())
        elif setop==7:
        elif setop==8:
            del(sett)
        elif setop==9:
            nlst=[]
            NL=int(input("enter number of ele in the new set..."))
            for i in range(NL):
               nle=int(input("enter ele in the new set..."))
               nlst.append(nle)
            nset=set(nlst)
            aftr=sett.union(nset)
            print(" union of sets is ==>",aftr)
        elif setop==10:
            nlst=[]
            NL=int(input("enter number of ele in the new set..."))
            for i in range(NL):
               nle=int(input("enter ele in the new set..."))
               nlst.append(nle)
            nset=set(nlst)
            aftr=sett.intersection(nset)
            print(" intersection of sets is  ==>",aftr)
        elif setop==11:
            nlst=[]
            NL=int(input("enter number of ele in the new set..."))
            for i in range(NL):
               nle=int(input("enter ele in the new set..."))
               nlst.append(nle)
            nset=set(nlst)
            aftr=sett.difference(nset)
            print(" difference  of sets is ==>",aftr)
        elif setop==12:
            nlst=[]
            NL=int(input("enter number of ele in the new set..."))
            for i in range(NL):
               nle=int(input("enter ele in the new set..."))
               nlst.append(nle)
            nset=set(nlst)
            aftr=sett.isdisjoint(nset)
            print("isdisjoint of sets is  ==>",aftr)
        elif setop==13:
            nlst=[]
            NL=int(input("enter number of ele in the new set..."))
            for i in range(NL):
               nle=int(input("enter ele in the new set..."))
               nlst.append(nle)
            nset=set(nlst)
            aftr=sett.issubset(nset)
            print("Given set issubset  ==>",aftr)
        elif setop==14:
            nlst=[]
            NL=int(input("enter number of ele in the new set..."))
            for i in range(NL):
               nle=int(input("enter ele in the new set..."))
               nlst.append(nle)
            nset=set(nlst)
            aftr=sett.issuperset(nset)
            print(" Given set issuperset ==>",aftr)
        elif setop==15:
            nlst=[]
            NL=int(input("enter number of ele in the new set..."))
            for i in range(NL):
               nle=int(input("enter ele in the new set..."))
               nlst.append(nle)
            nset=set(nlst)
            aftr=sett.difference_update(nset)
            print(" difference_update of sets ==>",aftr)
        else:
            print("Enter the valid set operation")
            print("---------\nSet operations \n  1.Add \n  2.Update \n  3.Remove \n  4.Discard \n  5.pop \n  6.Clear \n  7.Copy \n  8.Delete \n  9.Union \n  10.Intersection \n  11.Difference \n  12.Is_disjoin \n  13.Is_subset \n  14.Is_superser \n  15.Difference_update \n ")
            setop=int(input("Enter operation do you want to"))


elif ds=="4":
    dic={}
    print("First create your Dictionary")
    L=int(input("Enter number of elements"))
    for ELE in range(L): 
        L_ele=input("Enter key...")
        L_val=input("Enter value...")
        dic[L_ele]=L_val
    print(dic)
    dicopn=int(input("Enter number of operation do you want to"))
    for op in range(dicopn):
        print("---------\nDictionary operations \n  1.Add \n  2.Update \n  3.Remove \n  4.Replace \n  5.Clear \n  6.Copy \n  7.Popitem \n  8.Sort \n  9.Keys \n  10.Values \n  11.Len \n   ")
        dicop=int(input("Enter operation do you want to"))
        if dicop==1:
            L_ele=input("Enter key to Add...")
            L_val=input("Enter value to Add...")
            dic[L_ele]=L_val
            print(dic)
        elif dicop==2:
            Ndic={}
            L=int(input("Enter number of elements"))
            for i in range(L): 
                L_ele=input("Enter key...")
                L_val=input("Enter value...")
                Ndic[L_ele]=L_val
            dic.update(Ndic)
            print(dic)
        elif dicop==3:
            pp=input("Enter ele to pop")
            if pp in dic:
                dic.pop(pp)
                print("Dictionary after pop==>",dic)
            else:
                print(" enter valid key to pop")
        elif dicop==4:    
            pp=input("Enter key's value to replace")
            nrep=input("Enter value to replace")
            if pp in dic:
                dic[pp]=nrep
                print("Dictionary after replace==>",dic)
            else:
                print(" enter valid key to replace")
        elif dicop==5:
            dic.clear()
            print(dic)
        elif dicop==6:
            nme=input("Enter name to copy the dictionary")
            ndic=dic.copy()
            dic.popitem()
            print(dic)
        elif dicop==8:
            sorted(dic)
            print(dic)
        elif dicop==9:
            
            print(dic.keys())
        elif dicop==10:
            
            print(dic.values())
        elif dicop==11:
            print(len(dic))
        else:
            print("Enter the valid Dictionary operation")
            print("---------\nDictionary operations \n  1.Add \n  2.Update \n  3.Remove \n  4.Replace \n  5.Clear \n  6.Copy \n  7.Popitem \n  8.Sort \n  9.Keys \n  10.Values \n  11.Len \n   ")
            dicop=int(input("Enter operation do you want to"))
