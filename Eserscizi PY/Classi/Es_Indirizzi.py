import math

class IPadress():
    def __init__(self,ip_stringa):
        self.ip_notazione_dec = ip_stringa
        self.ip_notazione_bin = None
        self.ip_Broadcast = None
        self.ip_Rete = None
    
    def ip_broadcast(self,subnet_mask = "/22"):
        num = int(subnet_mask[1:])
        sub_bin = ""
        sub_bin = "0"*num + "1"*(32-num)
        """
        for w in range(0,32):
            if(w < num):
                sub_bin = sub_bin+"0"
            else:
                sub_bin = sub_bin+"1"
        """
        temp = ""
        for a in range(0,32):
            if(a % 8 == 0):
                temp =temp + "."
            else:
                pass
            if(self.ip_notazione_bin[a] == "0" and sub_bin[a] == "0"):
                temp = temp + '0'
            else:
                temp = temp + '1'

        self.ip_Broadcast=temp[1:]    
        return self.ip_Broadcast

    def ip_rete(self,subnet_mask = "/22"):
        num = int(subnet_mask[1:])
        sub_bin = ""
        sub_bin = "1"*num + "0"*(32-num)
        temp = ""
        for a in range(0,32):
            if(a % 8 == 0):
                temp =temp + "."
            else:
                pass
            if(self.ip_notazione_bin[a] == "1" and sub_bin[a] == "1"):
                temp = temp + '1'
            else:
                temp = temp + '0'

        self.ip_Rete=temp[1:]
            
        return self.ip_Rete

    def sottorete(self,sotto = "2",subnet_mask = "/22"):
        a = int(bin(sotto))
        b = int(sotto)
        for c in range(0,b):
            pass


    def dec2bin(self):
        lista_bin=self.ip_notazione_dec.split(".")
        lista_grupp = [int(Bin)for Bin in lista_bin]
        s = ""
        self.ip_notazione_bin = ""
        for gruppo in lista_grupp:
            temp= bin(gruppo)[2:]
            temp = "0"*(8-len(temp))+temp
            self.ip_notazione_bin = self.ip_notazione_bin+temp
            s = s +temp + "."
        return s[:-1]

    
def bin2dec(Ip):
    lista_bin_Rete=Ip.split(".")
    d = ""
    for num in lista_bin_Rete:
        temp = int(num,2)
        d = d + str(temp) +"."
    return d[:-1]
            
    #def toList(self):
    #    lista_stringhe = self.ip_notazione_dec.split(".")
    #    return[int(gruppo)for gruppo in lista_stringhe]

def decbin(sub):
    lista_bin=sub.split(".")
    lista_grupp = [int(Bin)for Bin in lista_bin]
    s = ""
    bina = ""
    for gruppo in lista_grupp:
        temp= bin(gruppo)[2:]
        temp = "0"*(8-len(temp))+temp
        bina = bina + temp
    cont = 0
    for a in range(0,32):
        if(bina[a] == "1"):
            cont = cont + 1
        else:
            pass
    s = ""
    s = "/"+str(cont)
    return s

def main():
    ip_Utente = input("Indirizzo IP: ")
    subnet_mask = input("Subnet Mask: ")
    if subnet_mask[0] == "/":
        pass
    else:
       subnet_mask = decbin(subnet_mask)
    indirizzoIP = IPadress(ip_Utente)
    #print(f"{indirizzoIP.ip_notazione_dec},{indirizzoIP.ip_notazione_bin}")
    #print(f"{indirizzoIP.toList()}")
    print(f"IP decimale: {indirizzoIP.ip_notazione_dec}")
    print(f"IP binario: {indirizzoIP.dec2bin()}\n")
    print(f"IP broadcast decimale: {bin2dec(indirizzoIP.ip_broadcast(subnet_mask))}")
    print(f"IP rete decimale: {bin2dec(indirizzoIP.ip_rete(subnet_mask))}")

if __name__ == "__main__":
    main()