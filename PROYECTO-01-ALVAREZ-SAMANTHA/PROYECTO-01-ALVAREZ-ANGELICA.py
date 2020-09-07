#Datos
from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches

#Usuarios registrados
Usuarios_Admin=[["Admin1","123"],["Admin2","234"],["Admin3","345"]] #Lista de administradores
Usuarios_Clientes=[["Cliente1","567"],["Cliente2","678"]]  #Lista de clientes

##LOGIN USUARIO/ADMINISTRADOR
intento=0 #Inicio contador de intentos
admin=False #bandera
cliente=False #bandera
while intento<3: 
     Usuario_inp=input("Usuario: ") #Solicita usuario 
     Contrasena_inp=input("Contraseña: ") #Solicita contraseña
     #Verifica si el ingreso es de un Administrador
     for usuario_a in Usuarios_Admin:
         if usuario_a[0]==Usuario_inp:
             if usuario_a[1]==Contrasena_inp:
                 admin=True
                 intento=3
                 break
             else:
                 print("Contraseña incorrecta."+ " Te quedan:"+str(3-intento-1)+" intentos")
                 admin=True
                 break
         else:
            admin=False
            continue
      #Verifica si el ingreso es de un Cliente
     if admin==False:
         for usuario_c in Usuarios_Clientes:
             if usuario_c[0]==Usuario_inp:
                 if usuario_c[1]==Contrasena_inp:
                     print("No tiene permitido el acceso.")
                     print("Visita la pagina www.life_store.com para conocer nuestros productos")
                     cliente=True
                     break
                 else:
                     print("Contraseña incorrecta."+ " Te quedan:"+str(3-intento-1)+" intentos")
                     cliente=True
                     break
             else:
                 cliente=False
                 continue
     #Avisa si no se encuentra el usuario
     if cliente==False and admin==False:
         print("No se encontro al usuario."+ " Te quedan:"+str(3-intento-1)+" intentos")
     intento+=1
     #Avisa si ya se acabaron los intentos
     if intento==3 and cliente==False:
         admin=False
         print("Ya se realizaron 3 intentos. Vuelva mas tarde")
   
while admin==True:
    #Inicio de listas con contadores
    vend = [0]*len(lifestore_products) #ventas
    devol = [0]*len(lifestore_products) #devoluciones
    reseña= [0]*len(lifestore_products) #reseñas
    vend_mensual=[0]*12 #ventas mensuales
    devol_mensual=[0]*12 #devoluciones mensuales
    unidades_devol=0 #Unidades devueltas
    busq= [0]*len(lifestore_products) #busquedas
    
    #Contar ventas, devoluciones y sumar reseñas
    for sales in lifestore_sales:
        vend[sales[1]-1] += 1
        reseña[sales[1]-1] += sales[2]
        vend_mensual[int(sales[3][3:5])-1]+=lifestore_products[sales[1]-1][2]
        if sales[4]==1:
            devol[sales[1]-1] += 1
            unidades_devol+=1
            devol_mensual[int(sales[3][3:5])-1]+=lifestore_products[sales[1]-1][2]
    
    #Contar busquedas
    for search in lifestore_searches:
        busq[search[1]-1] +=1
    
        
    #OPTENCION DE LISTAS 
    categorias=[] #categorias=[categoria] 
    ventas= [] #ventas=[unidades.vendidas,producto,ingreso,categoria, stock ]
    busquedas= [] #busquedas=[busquedas,producto,unidades.vendidas,categoria]
    calificacion=[] #calificacion=[calificacion.prom,producto,devoluciones]
    
    #Agregado de datos para ventas, busquedas y calificacion
    for productos in lifestore_products:
        #categorias de los productos
        if productos[3] not in categorias:
            categorias.append(productos[3]) 
        #ventas
        lista=[vend[productos[0]-1],productos[1],productos[2]*vend[productos[0]-1],productos[3],productos[4]]
        ventas.append(lista)
        #busquedas
        lista=[busq[productos[0]-1],productos[1],vend[productos[0]-1],productos[3]]
        busquedas.append(lista)
        #calificaciones de los productos
        if vend[productos[0]-1]==0:
            lista=[0,productos[1],devol[productos[0]-1]]
            calificacion.append(lista)
            continue
        lista=[reseña[productos[0]-1]/vend[productos[0]-1],productos[1],devol[productos[0]-1]]
        calificacion.append(lista)
      
      
    ventas_anual=0 #Ingreso ventas al año
    devoluciones_anual=0 #Perdida devoluciones al año  
    ventas_mensuales=[] #ventas_mensuales=[ventas,mes,devoluciones,total] 
    meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    #Agregado de datos para ingresos
    for i in range(12):
        lista=[vend_mensual[i],meses[i],devol_mensual[i],vend_mensual[i]-devol_mensual[i]]
        ventas_anual+=vend_mensual[i] 
        devoluciones_anual+=devol_mensual[i]
        ventas_mensuales.append(lista)
    
    ventas_totales=ventas_anual-devoluciones_anual #Ingreso total
    
 
    #Mostrar opciones al administrador
    mostrar=True
    while mostrar==True:
        print("Opciones:\n1) Productos\n2) Reseñas de productos \n3) Ingresos ")
        Opcion=input("Elige una opción: ")
        #PRODUCTOS
        if Opcion=="1":
            error=True #bandera
            while error==True:
                #Opciones de productos
                print("Opciones:\n1) Productos mas vendidos\n2) Productos menos vendidos \n3) Productos mas buscados \n4) Productos menos buscados")
                Opcion_ventas=input("Elige una opción: ")
                if Opcion_ventas=="1":
                     print("PRODUCTOS MÁS VENDIDOS: \n")
                     sub_error=True #bandera
                     while sub_error==True:
                         ventas.sort(reverse=True) 
                         #Opciones de productos mas vendidos
                         ventas_select=input("Opciones:\n1) General \n2) Por categoria \n Elige una opcion: ")
                         if ventas_select=="1":
                             print("PRODUCTOS MÁS VENDIDOS: \n")
                             n_veces=0
                             while n_veces<50 and ventas[n_veces][0]!=0:
                                 print(str(n_veces+1)+" " +ventas[n_veces][1])#Nombre del producto
                                 #calcula el % de unidades vendidas con respecto del total del producto
                                 porcentaje_unidades=str('{:.2f}'.format(ventas[n_veces][0]*100/len( lifestore_sales)))
                                 print("Unidades Vendidas: "+str(ventas[n_veces][0]) +" (% Total: "+porcentaje_unidades+"%)")
                                 #calcula el % de ingreso con respecto del total del producto
                                 porcentaje_ventas=str('{:.2f}'.format(ventas[n_veces][2]*100/ventas_anual))
                                 print("Ventas: $"+str(ventas[n_veces][2])+" (% Total: "+porcentaje_ventas+"%) \n")
                                 n_veces+=1
                             sub_error=False
                         elif ventas_select=="2":
                             print("PRODUCTOS MÁS VENDIDOS POR CATEGORIA: \n")
                             for categoria in categorias:
                                 porcentaje_unidades=0 #Inicio contador de %unidades vendidas por categoria
                                 porcentaje_ventas=0  #Inicia contador de %ingresos por categoria
                                 n_veces=0
                                 print("CATEGORIA: "+categoria)
                                 for venta in ventas:
                                     if venta[3]==categoria and venta[0]!=0:
                                         print(str(n_veces+1)+" "+venta[1]) #Nombre del producto
                                         print("Unidades Vendidas: "+str(venta[0]))
                                         print("Total: $"+str(venta[2])+"\n")
                                         n_veces+=1
                                         porcentaje_unidades+=venta[0]/len( lifestore_sales) #unidades.vendidas/total.de.ventas
                                         porcentaje_ventas+=venta[2]/ventas_anual #ventas/ingreso.total
                                 print("% de unidades vendidas: "+str('{:.2f}'.format(porcentaje_unidades*100))+"%")
                                 print("% de ventas: "+str('{:.2f}'.format(porcentaje_ventas*100))+"% \n\n")
                             sub_error=False
                         else:
                             print("Error. El valor ingresado no se encuentra dentro de las opciones\n")          
                     error=False
                elif Opcion_ventas=="2":
                    sub_error=True #bandera
                    while sub_error==True:
                        print("PRODUCTOS MENOS VENDIDOS: \n")
                        ventas.sort() 
                        #Opciones de productos menos vendidos
                        ventas_select=input("Opciones:\n1) General \n2) Por categoria \n Elige una opcion: ")
                        if ventas_select=="1":
                            print("PRODUCTOS MENOS VENDIDOS: \n")
                            n_veces=0
                            while n_veces<50 or ventas[n_veces][0]==0:
                                print(str(n_veces+1)+" " +ventas[n_veces][1])#Nombre del producto
                                print("Unidades Vendidas: "+str(ventas[n_veces][0]))
                                print("Total: $"+str(ventas[n_veces][2])+"\n")
                                n_veces+=1
                            sub_error=False
                        elif ventas_select=="2":
                            print("PRODUCTOS MENOS VENDIDOS POR CATEGORIA: \n")
                            i=0 #indice
                            for categoria in categorias:
                                n_veces=0
                                print("CATEGORIA: "+categoria)
                                for venta in ventas:
                                    if venta[3]==categoria and venta[0]==0: 
                                        print(str(n_veces+1)+" "+venta[1])#Nombre del producto
                                        print("Unidades Vendidas: "+str(venta[0])+"\n")
                                        n_veces+=1
                                i+=1
                                print("\n")
                            sub_error=False
                        else:
                            print("Error. El valor ingresado no se encuentra dentro de las opciones\n")           
                    error=False         
                elif Opcion_ventas=="3":
                     sub_error=True #bandera
                     while sub_error==True:
                         print("PRODUCTOS MÁS BUSCADOS: \n")
                         busquedas.sort(reverse=True)
                         #Opciones de productos mas buscados
                         busquedas_select=input("Opciones:\n1) General \n2) Por categoria \n Elige una opcion: ")
                         if busquedas_select=="1":
                             print("PRODUCTOS MÁS BUSCADOS: \n")
                             n_veces=0
                             while busquedas[n_veces][0]!=0:
                                 print(str(n_veces+1)+" " +busquedas[n_veces][1])#nombre del producto
                                 print("Busquedas: "+str(busquedas[n_veces][0]))
                                 print("Unidades vendidas: "+str(busquedas[n_veces][2])+"\n")
                                 #calcula las busquedas que concluyen en ventas
                                 porcentaje_busqueda=busquedas[n_veces][2]*100/busquedas[n_veces][0] #ventas/busquedas
                                 print("% que concluye en venta: "+ str('{:.2f}'.format(porcentaje_busqueda))+"%\n\n")
                                 n_veces+=1
                             sub_error=False
                         elif busquedas_select=="2":
                             print("PRODUCTOS MÁS BUSCADOS POR CATEGORIA: \n")
                             for categoria in categorias:
                                 n_veces=0
                                 numero_ventas=0 #Inicia contador de ventas
                                 numero_busqueda=0 #Inicia contador de busquedas
                                 print("CATEGORIA: "+categoria)
                                 for busqueda in busquedas:
                                     if busqueda[3]==categoria and  busqueda[0]!=0:
                                         print(str(n_veces+1)+" "+busqueda[1])#Nombre del producto
                                         print("Busquedas: "+str(busqueda[0]))
                                         print("Unidades vendidas: "+str(busqueda[2]))
                                         numero_ventas+=busqueda[2]
                                         numero_busqueda+=busqueda[0]
                                         n_veces+=1
                                 if numero_busqueda==0: 
                                     print("No se realizaron busquedas en esta categoria\n\n")
                                     continue
                                 #calcula las busquedas que concluyen en ventas
                                 porcentaje_busqueda=numero_ventas*100/numero_busqueda
                                 print("\n% que concluye en venta: "+str('{:.2f}'.format(porcentaje_busqueda)))
                                 #calcula la participacion de busquedas de cada categoria
                                 participacion_busquedas=numero_busqueda
                                 print("Busquedas realizadas: "+str('{:.2f}'.format(participacion_busquedas))+"\n\n")
                             sub_error=False
                         else:
                             print("Error. El valor ingresado no se encuentra dentro de las opciones\n")
                             
                     error=False
                elif Opcion_ventas=="4":
                    sub_error=True #bandera
                    while sub_error==True:
                        print("PRODUCTOS MENOS BUSCADOS: \n")
                        busquedas.sort() 
                        #Opciones de productos menos buscados
                        busquedas_select=input("Opciones:\n1) General \n2) Por categoria \n3 Elige una opcion: ")
                        if busquedas_select=="1":
                            n_veces=0
                            while n_veces<50 and busquedas[n_veces][0]==0:
                                print(str(n_veces+1)+" " +busquedas[n_veces][1])#Nombre del producto
                                print("Busquedas: "+str(busquedas[n_veces][0]))
                                print("Unidades vendidas: "+str(busquedas[n_veces][2])+"\n")
                                n_veces+=1
                            sub_error=False
                        elif busquedas_select=="2":
                            print("PRODUCTOS MENOS BUSCADOS POR CATEGORIA: \n")
                            for categoria in categorias:
                                n_veces=0
                                print("CATEGORIA: "+categoria)
                                for busqueda in busquedas:
                                    if busqueda[3]==categoria and  busqueda[0]==0:
                                        print(str(n_veces+1)+" "+busqueda[1])#Nombre del producto
                                        print("Busquedas: "+str(busqueda[0]))
                                        print("Unidades vendidas: "+str(busqueda[2])+"\n")
                                        n_veces+=1
                                print("Productos no buscados: "+ str(n_veces))
                            print("\n\n") 
                            sub_error=False
                        else:
                            print("Error. El valor ingresado no se encuentra dentro de las opciones\n") 
                    error=False
                else:
                    print("Error. El valor ingresado no se encuentra dentro de las opciones\n")
            mostrar=False
        #RESEÑAS
        elif Opcion=="2":
            error=True #bandera
            while error==True:
                #Opciones de reseñas
                print("Opciones:\n1) Mejores reseñas\n2) Peores reseñas")
                Opcion_reseñas=input("Elige una opción: ")
                if Opcion_reseñas=="1":
                     print("PRODUCTOS MEJOR CALIFICADOS: \n")
                     calificacion.sort(reverse=True)
                     n_veces=0
                     while n_veces<20:
                         print(str(n_veces+1)+" " +calificacion[n_veces][1])#Nombre del producto
                         print("Calificacion de los usuarios: "+str('{:.2f}'.format(calificacion[n_veces][0])))
                         print("Unidades Devueltas: "+str(calificacion[n_veces][2])+"\n")
                         n_veces+=1
                     error=False
                elif Opcion_reseñas=="2":
                     print("PRODUCTOS PEOR CALIFICADOS: \n")
                     calificacion.sort()
                     n_veces=0
                     i=0
                     while n_veces<20:
                         if calificacion[i][0]==0:
                             i+=1
                             continue
                         print(str(i+1)+" " +calificacion[i][1])#Nombre del producto
                         print("Calificacion de los usuarios: "+str('{:.2f}'.format(calificacion[i][0])))
                         print("Unidades Devueltas: "+str(calificacion[i][2])+"\n")
                         i+=1
                         n_veces+=1
                     error=False
                else:
                    print("Error. El valor ingresado no se encuentra dentro de las opciones\n")
            mostrar=False       
        #INGRESOS
        elif Opcion=="3":
            print("Ingresos")
            error=True #bandera
            while error==True:
                #Opciones de ingresos
                print("Opciones:\n1) Ingresos mensuales\n2) Ventas vs Inventario \n3) Resumen de ingresos")
                Opcion_ventas_mensuales=input("Elige una opción: ")
                if Opcion_ventas_mensuales=="1":
                     n_veces=0
                     while n_veces<12:
                         print("Mes: "+ ventas_mensuales[n_veces][1])
                         print("Ventas: $"+ str(ventas_mensuales[n_veces][0]))
                         print("Devoluciones: $"+ str(ventas_mensuales[n_veces][2]))
                         print("TOTAL: $"+ str(ventas_mensuales[n_veces][3])+'\n')
                         n_veces+=1
                     error=False
                elif Opcion_ventas_mensuales=="2":
                    #Ventas vs inventarios de productos mas vendidos
                    print("MAS VENDIDOS")
                    ventas.sort(reverse=True) 
                    n_veces=0
                    while n_veces<8:
                         print(str(n_veces+1)+" " +ventas[n_veces][1])#nombre del producto
                         print("Ventas: "+ str(ventas[n_veces][0]))
                         print("Stock: "+ str(ventas[n_veces][4]))
                    
                         n_veces+=1
                    print("\n\n MENOS VENDIDOS")
                    #Ventas vs inventarios de productos menos vendidos
                    menos_vendidos=[] #menos_vendidos[stock,producto,unidades vendidas]
                    for venta in ventas:
                        if venta[0]==0:
                            lista=[venta[4],venta[1],venta[0]]
                            menos_vendidos.append(lista)
                    menos_vendidos.sort(reverse=True)
                    n_veces=0
                    while n_veces<8:
                         print(str(n_veces+1)+" " +menos_vendidos[n_veces][1])#Nombre del producto
                         print("Ventas: "+ str(menos_vendidos[n_veces][2]))
                         print("Stock: "+ str(menos_vendidos[n_veces][0]))
                         n_veces+=1
                
                    error=False
                     
                elif Opcion_ventas_mensuales=="3":
                    ventas_mensuales.sort(reverse=True) #ordena las ventas mensuales
                    print("LifeStore 2020")
                    print("Ventas al año:\n  Unidades:"+str(len(lifestore_sales))+" Ingreso: $"+ str(ventas_anual))                   
                    print("Devoluciones al año:\n  Unidades:"+str(unidades_devol)+" Perdida: $"+ str(devoluciones_anual))
                    print("Ventas Totales: $"+ str('{:.2f}'.format(ventas_totales)))
                    print("Ventas mensuales promedio: $"+ str('{:.2f}'.format(ventas_totales/12)))
                    print("5 Meses con mayores ventas: ")
                    n_veces=0
                    #imprime 5 meses con mayores ventas
                    while n_veces<5:
                        print("  "+ventas_mensuales[n_veces][1]+ ".  Ventas: $"+ str(ventas_mensuales[n_veces][0])+'\n')
                        n_veces+=1
                    error=False   
            
                else:
                    print("Error. El valor ingresado no se encuentra dentro de las opciones\n")
            mostrar=False
        else:
            print("Error. El valor ingresado no se encuentra dentro de las opciones\n")
    
    consultar=True
    #Pregunta al usuario si desea consultar otro apartado
    while consultar==True:
        consulta=input("Deseas realizar otra consulta (Si/No): ")
        if consulta=="No":
            admin=False
            consultar=False
        elif consulta=="Si":
            admin=True
            consultar=False
        else:
            print("Error. El valor ingresado no se encuentra dentro de las opciones\n")
        

    
        
