graph = {'Batununggal': ['Lengkong', 'Kiara Condong','Buah Batu','Sumur Bandung','Cibeunying Kidul'],
             'Cibeunying Kidul': ['Kiara Condong', 'Cibeunying Kaler','Bandung Wetan','Sumur Bandung','Batununggal'],
             'Sumur Bandung': ['Batununggal','Cibeunying Kidul','Bandung Wetan'],
             'Bandung Wetan': ['Cibeunying Kaler','Cibeunying Kidul','Sumur Bandung'],
             'Kiara Condong': ['Antapani','Batununggal','Cibeunying Kidul'],
             'Cibeunying Kaler': ['Cibeunying Kidul','Bandung Wetan'],
             'Buah Batu': ['Batununggal'],
             'Lengkong': ['Batununggal'],
             'Antapani': ['Kiara Condong'],
         }
 
def jalur_terpendek(graph, awal, tujuan, jalur=[]):
        jalur = jalur + [awal]
        if awal == tujuan:
            return jalur
        if not graph.has_key(awal):
            return None
        jalurpendek = None
        for node in graph[awal]:
            if node not in jalur:
                newjalur = jalur_terpendek(graph, node, tujuan, jalur)
                if newjalur:
                    if not jalurpendek or len(newjalur) < len(jalurpendek):
                        jalurpendek = newjalur
        return jalurpendek
print("Jalur Kecamatan Kota Bandung")
print ("(Batununggal,Cibeunying Kidul,Sumur Bandung,Kiara Condong)")
print ("(Cibeunying Kaler,Buah Batu,Lengkong,Antapani)")
print ("\n")
awal = raw_input("Masukan Awal : ")
tujuan = raw_input("Masukan Tujuan : ")
hasil = jalur_terpendek(graph, awal, tujuan, jalur=[])
print "Jalur Terpendek", hasil
