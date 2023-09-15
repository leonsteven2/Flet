import flet
from flet import Page, Text, TextField, Row, ElevatedButton, Column

def main(page: Page):
    page.title = "Cálculo Acumulador"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    txt_masa = TextField(value="200",label="Masa (Kg)",width=150)
    txt_carrera = TextField(value="3",label="Carrera (m)",width=150)
    txt_caudal_bomba = TextField(value="2",label="Caudal Bomba (L/min)",width=250)
    txt_presion_trabajo_estimada =  TextField(value="60",label="Presion Trabajo Estimada (bar)",width=200)
    txt_rozamiento = TextField(value="1.1",label="Rozamiento",width=150)
    txt_perdidas = TextField(value="1.5",label="Perdidas Mecanicas",width=150)
    txt_area_disponible_piston = TextField(value=19.63, label="Área disponible del Pistón (cm2)", width=250)
    txt_presion_perdida_bomba = TextField(value=14, label="Presión Perdida Bomba (bar)", width=250)
    txt_presion_perdida_limitadora = TextField(value=10, label="Presión Perdida Limitadora (bar)", width=250)
    txt_p0 = TextField(value=18, label="P0", width=100)
    txt_p1 = TextField(value=20, label="P1", width=100)
    txt_p2 = TextField(value=40, label="P2", width=100)

    def calculo_acumulador(event):
        volumen_descarga = float(txt_carrera.value)*100*float(txt_area_disponible_piston.value)
        volumen_v2 = -volumen_descarga/(1-(float(txt_p2.value)/float(txt_p1.value))**(1/1.4))
        volumen_v0 = (   (float(txt_p2.value)*(volumen_v2**1.4))/(float(txt_p0.value))   )**(1/1.4)
        v0_litros = round(volumen_v0/1000,2)

        lbl_v0 = Text(f'El volumen del acumulador es: {v0_litros} litros')
        col_main.controls.append(lbl_v0)
        page.update()

    def calculo_presion_bomba_limitadora(event):
        col_main.spacing = 15

        lbl_presion_bomba = Text(f'La presión de la bomba es: {round(( float(txt_masa.value)*9.8*float(txt_perdidas.value)*float(txt_rozamiento.value)  )/( float(txt_area_disponible_piston.value)/10000*100000  ) + float(txt_presion_perdida_bomba.value),2) } bar',color="red")
        col_main.controls.append(lbl_presion_bomba)

        lbl_presion_limitadora = Text(f'La presión en la limitadora es: {round(( float(txt_masa.value)*9.8*float(txt_perdidas.value)*float(txt_rozamiento.value)  )/( float(txt_area_disponible_piston.value)/10000*100000  ) + float(txt_presion_perdida_bomba.value),2) + float(txt_presion_perdida_limitadora.value)} bar',color="red")
        col_main.controls.append(lbl_presion_limitadora)

        velocidad = round(  (float(txt_caudal_bomba.value)*1000/60)/(txt_area_disponible_piston.value)  ,2)
        lbl_velocidad_piston = Text(f'La velocidad del pistón es: { velocidad } cm/seg', color="blue")
        col_main.controls.append(lbl_velocidad_piston)

        lbl_tiempo = Text(f'El tiempo que tarda en recorrer {txt_carrera.value} metros es: {   round(   float(txt_carrera.value)*100/velocidad*1/60   ,2)   } min',color="blue")
        col_main.controls.append(lbl_tiempo)

        row_px = Row([
            txt_p0,
            txt_p1,
            txt_p2,
            ElevatedButton("Calcular Acumulador",on_click=calculo_acumulador)
        ],alignment="center")

        col_main.controls.append(row_px)

        page.update()

    def calculo_presion_trabajo(event):

        lbl_presion_trabajo = Text(f'La presión de trabajo es: {round(( float(txt_masa.value)*9.8*float(txt_perdidas.value)*float(txt_rozamiento.value)  )/( float(txt_area_disponible_piston.value)/10000*100000  ),2)} bar',color="red")
        row_presiones_perdidas = Row(
            [
                txt_presion_perdida_bomba,
                txt_presion_perdida_limitadora,
                ElevatedButton("Calcular Presión Bomba y Limitadora", on_click=calculo_presion_bomba_limitadora)
            ],alignment="center"
        )

        col_main.controls.append(lbl_presion_trabajo)
        col_main.controls.append(row_presiones_perdidas)
        page.update()


    def calculo_area_piston(event):
        lbl_area_piston = Text(f'El área del piston es {round((float(txt_masa.value)*9.8*float(txt_rozamiento.value)*float(txt_perdidas.value))/(float(txt_presion_trabajo_estimada.value)*100000)*10000,2)} cm2',color="red")
        row_proceso2 = Row(
            [
               txt_area_disponible_piston,
               ElevatedButton("Calcular Presión de Trabajo",on_click=calculo_presion_trabajo),
            ],
            alignment="center"
        )
        col_main.controls.append(lbl_area_piston)
        col_main.controls.append(row_proceso2)
        page.update()

    Datos_Ejercicio = Row([
        txt_masa,
        txt_carrera,
        txt_caudal_bomba,
        txt_presion_trabajo_estimada,
        txt_rozamiento,
        txt_perdidas,
        ElevatedButton("Cálcular área del piston", on_click=calculo_area_piston)
    ], alignment="center")

    col_main = Column([
               Text("DATOS DEL EJERCICIO"),
               Datos_Ejercicio,

               ],spacing=30, horizontal_alignment="center"
            )

    page.add(
        col_main
    )

flet.app(target=main)