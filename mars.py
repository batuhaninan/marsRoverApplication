from Plato import Plato

"""
    size: (COLUMN,ROW)
        Map'in size'i

    position: (X,Y)
        Başlama pozisyonu (Center = True ise override edilir)

    direction: n w s e
        Başlama yönü (Default = n)

    center: True - False
        Rover map'in ortasında mı spawn olsun? (True ise position override edilir)

    printStage: True - False
        Her aşama sonrasında map print edilsin mi?

    deleteOnInstruction : True - False
        Her instruction sonrasında map reset'lensin mi?

    NOT: Eger center verilirse position degeri override edilir!

"""
 
		
plato = Plato(size=(5,5), position=(1,3), direction="n", center=True, printStage=True, deleteOnInstruction=True)
y, x = plato.instructions("m")
y1, x1 = plato.instructions("ml")
