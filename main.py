import flet as ft


def main(page: ft.Page):
    # Configuraciones de la página matias
    page.title = "Ushuaia ONG"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO
    page.theme = ft.Theme(
        font_family="Verdana")
    page.bgcolor = ft.colors.BLUE_GREY_100

    # Fuentes personalizadas
    page.fonts = {
        "Pacifico": "/Pacifico-Regular.ttf",
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
    }

    # Imagenes
    image_files = [
        ("Pequeñospasos.png", "https://www.instagram.com/pequenos_pasos/reel/C7CMjXZruBz/"),
        ("Fundacionnep.jpg", "http://www.fundacionnep.org.ar/index.html"),
    ]

    # Carrusel de imágenes
    carrusel = ft.Container(
        content=ft.Row(
            controls=[],  # Lista vacía para almacenar las imágenes
            scroll="always",  # Scroll horizontal para el carrusel
            alignment=ft.MainAxisAlignment.CENTER,

        ),
        alignment=ft.alignment.top_center,
        padding=20,
        expand=True,
    )

    # Añadir las imágenes al carrusel utilizando for
    for src, url in image_files:
        imagen = ft.IconButton(
                content=ft.Image(
                    src=src,
                    width=400,
                    height=300,
                ),
                on_click=lambda e, url=url: page.launch_url(url)
            )
        carrusel.content.controls.append(imagen)

    # Función para mostrar el carrusel al hacer clic en "Inicio"
    def view_inicio(e):
        page.clean()
        page.add(titulo, carrusel)
        page.update()

    # Función para mostrar educacion al hacer clic en "Educación"
    def view_educacion(e):
        page.clean()
        page.add(educacion)
        page.update()
    # Función para mostrar al hacer clic en "Salud"
    def view_salud(e):
        page.clean()
        page.add(salud)
        page.update()
    
    def view_animales(e):
        page.clean()
        page.add(animales)
        page.update()

    def view_medio_ambiente(e):
        page.clean()
        page.add(MedioAmbiente)
        page.update()

    def view_ayuda_social(e):
        page.clean()
        page.add(ayuda_social)
        page.update()

    
    
    



         #Listado de Salud
    ong_salud = [
        {
            "nombre": "ASDU Asociación Síndrome de down de Ushuaia ",
            "descripcion":"La Asociación Síndrome de Down de Ushuaia ASDU es presidida por Viviana Borrego. El programa de deportes de la asociación es llevado adelante por Alejandro Maldonado.Último proyecto: charla abierta (10/11/17)Dedicada a las familias ,amigos, conocidos y público en general sobre la capacitación de discapacidad.",
            "facebook": "https://www.facebook.com/share/uZLp639Lq4saxCPE/",  
            "instagram": "",  
            "pagina_web": "http://www.asdu.com.ar/",
        }
    ]

    salud = ft.Container(
        content=ft.ResponsiveRow(
            controls=[],  # Lista vacía para rellenar con tarjetas
            col={"sm": 12, "md": 12, "xl": 12}
        ),
        padding=5,
        margin=25,
        border_radius=15
    )

    for ong in ong_salud:
        # Tarjeta para cada ONG
        tarjeta = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            title=ft.Text(
                                ong["nombre"], color="Black", size=16, weight="bold"),
                            subtitle=ft.Text(
                                ong["descripcion"],
                                text_align="justify", color="Black"
                            ),
                        ),
                        ft.Row(
                            [
                                # Botón para WhatsApp
                                ft.TextButton(
                                    content=ft.Image(
                                        src="whatsapp.jpg", width=32, height=32, tooltip="WhatsApp"),
                                    on_click=lambda e: page.launch_url(
                                        ong["whatsapp"])
                                ),
                                # Botón para Facebook
                                ft.TextButton(
                                    content=ft.Image(
                                        src="facebook.png", width=32, height=32, tooltip="Facebook"),
                                    on_click=lambda e: page.launch_url(
                                        ong["facebook"])
                                ),
                                # Botón para Instagram
                                ft.TextButton(
                                    content=ft.Image(
                                        src="instagram.jpg", width=32, height=32, tooltip="Instagram"),
                                    on_click=lambda e: page.launch_url(
                                        ong["instagram"])
                                )
                            ]
                        ),
                        ft.Row(
                            [
                                ft.TextButton(
                                    "Más información", 
                                    on_click=lambda e: page.launch_url(ong["pagina_web"]),
                                    icon = ft.icons.ARROW_CIRCLE_RIGHT_SHARP
                                    ),
                                    # Botón de Ubicacion
                                ft.TextButton(
                                    "Ubicación",
                                    on_click=lambda e: page.launch_url(ong["ubicación"]),
                                    icon = ft.icons.LOCATION_ON),
                                
                            ]
                        ),
                        
                    ]
                ),
                width=400,
                padding=10,
                bgcolor="white",
                border_radius=10
            ),
            col={"sm": 12, "md": 6, "xl": 4}
        )

        salud.content.controls.append(tarjeta)


    # Listado de Educacion
    ong_educacion = [
        {
            "nombre": "Pequeños pasos",
            "descripcion": "La ONG Pequeños Pasos es una organización que se centra en brindar ayuda a niños y niñas en condiciones de vulnerabilidad y abandono. Su misión es desarrollar habilidades sociales resilientes en las áreas de educación, salud, nutrición, trabajo e integración.",
            "whatsapp": "https://wa.me/01147354910",  
            "facebook": "https://www.facebook.com/pequenospasosargentina/?locale=es_LA",  
            "instagram": "https://www.instagram.com/pequenos_pasos/?hl=es%20",  
            "pagina_web": "https://pequenospasos.com/",
            "ubicación": ""
        }
    ]

    
    educacion = ft.Container(
        content=ft.ResponsiveRow(
            controls=[],  # Lista vacía para rellenar con tarjetas
            col={"sm": 12, "md": 12, "xl": 12}
        ),
        padding=5,
        margin=25,
        border_radius=15
    )

    # Añadir las tarjetas de ONG utilizando un bucle for
    for ong in ong_educacion:
        # Tarjeta para cada ONG
        tarjeta = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            title=ft.Text(
                                ong["nombre"], color="Black", size=16, weight="bold"),
                            subtitle=ft.Text(
                                ong["descripcion"],
                                text_align="justify", color="Black"
                            ),
                        ),
                        ft.Row(
                            [
                                # Botón para WhatsApp
                                ft.TextButton(
                                    content=ft.Image(
                                        src="whatsapp.jpg", width=32, height=32, tooltip="WhatsApp"),
                                    on_click=lambda e: page.launch_url(
                                        ong["whatsapp"])
                                ),
                                # Botón para Facebook
                                ft.TextButton(
                                    content=ft.Image(
                                        src="facebook.png", width=32, height=32, tooltip="Facebook"),
                                    on_click=lambda e: page.launch_url(
                                        ong["facebook"])
                                ),
                                # Botón para Instagram
                                ft.TextButton(
                                    content=ft.Image(
                                        src="instagram.jpg", width=32, height=32, tooltip="Instagram"),
                                    on_click=lambda e: page.launch_url(
                                        ong["instagram"])
                                )
                                
                                
                            ]
                        ),

                        ft.Row(
                            [
                                ft.TextButton(
                                    "Más información", 
                                    on_click=lambda e: page.launch_url(ong["pagina_web"]),
                                    icon = ft.icons.ARROW_CIRCLE_RIGHT_SHARP
                                    ),
                                    # Botón de Ubicacion
                                ft.TextButton(
                                    "Ubicación",
                                    on_click=lambda e: page.launch_url(ong["ubicación"]),
                                    icon = ft.icons.LOCATION_ON),
                                
                            ]
                        ),
                    ]
                ),
                width=400,
                padding=10,
                bgcolor="white",
                border_radius=10
            ),
            col={"sm": 12, "md": 6, "xl": 4}
        )

        # Añadir la tarjeta al contenedor (al ResponsiveRow dentro de "educacion")
        educacion.content.controls.append(tarjeta)

    ong_animales = [
        {
            "nombre": "Amigos Del Reino Animal Fueguino",
            "descripcion": "HACER RESPETAR los DERECHOS & NECESIDADES de los ANIMALES NO HUMANOS, su CUIDADO RESPONSABLE y el TRATO POSITIVO para todos ellos mediante Campañas de Concientización y participación en eventos.",
            "whatsapp" : "",
            "facebook": "https://www.facebook.com/share/oPSpEDLzWiNfttyR/?mibextid=qi2Omg",  
            "instagram": "https://www.instagram.com/araf.ushuaia?igsh=c3p0eDk4aG96Mm9o",  
            "pagina_web": "https://araf.com.ar/contacto.html"  
        }
    ]

    animales = ft.Container(
        content=ft.ResponsiveRow(
            controls=[],  # Lista vacía para rellenar con tarjetas
            col={"sm": 12, "md": 12, "xl": 12}
        ),
        padding=5,
        margin=25,
        border_radius=15
    )

    for ong in ong_animales:
        # Tarjeta para cada ONG
        tarjeta = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            title=ft.Text(
                                ong["nombre"], color="Black", size=16, weight="bold"),
                            subtitle=ft.Text(
                                ong["descripcion"],
                                text_align="justify", color="Black"
                            ),
                        ),
                        ft.Row(
                            [
                                # Botón para WhatsApp
                                ft.TextButton(
                                    content=ft.Image(
                                        src="/whatsapp.jpg", width=32, height=32, tooltip="WhatsApp"),
                                    on_click=lambda e: page.launch_url(
                                        ong["whatsapp"])
                                ),
                                # Botón para Facebook
                                ft.TextButton(
                                    content=ft.Image(
                                        src="facebook.png", width=32, height=32, tooltip="Facebook"),
                                    on_click=lambda e: page.launch_url(
                                        ong["facebook"])
                                ),
                                # Botón para Instagram
                                ft.TextButton(
                                    content=ft.Image(
                                        src="/instagram.jpg", width=32, height=32, tooltip="Instagram"),
                                    on_click=lambda e: page.launch_url(
                                        ong["instagram"])
                                )
                            ]
                        ),
                         ft.Row(
                            [
                                ft.TextButton(
                                    "Más información", 
                                    on_click=lambda e: page.launch_url(ong["pagina_web"]),
                                    icon = ft.icons.ARROW_CIRCLE_RIGHT_SHARP
                                    ),
                                    # Botón de Ubicacion
                                ft.TextButton(
                                    "Ubicación",
                                    on_click=lambda e: page.launch_url(ong["ubicación"]),
                                    icon = ft.icons.LOCATION_ON),
                                
                            ]
                        ),

                       
                    ]
                ),
                width=400,
                padding=10,
                bgcolor="white",
                border_radius=10
            ),
            col={"sm": 12, "md": 6, "xl": 4}
        )

        animales.content.controls.append(tarjeta)
    

    ong_MedioAmbiente = [
        {
            "nombre": "Asociacion Manekenk",
            "descripcion": "Nuestra organización no gubernamental se dedica a la Educación, la comunicación y la conservación ambiental, abordando cuestiones territoriales, ambientales y de áreas protegidas.",  
            "facebook": "https://www.facebook.com/Asociacion.Manekenk/?locale=es_LA",  
            "instagram": "https://www.instagram.com/manekenk/?hl=es-la",  
            "pagina_web": "https://www.manekenk.org.ar/"  
        }
    ]

        
    MedioAmbiente = ft.Container(
            content=ft.ResponsiveRow(
                controls=[ft.Text("MEDIO AMBIENTE", color=ft.colors.BLACK,
                        font_family="Verdana", text_align="start"),],  # Lista vacía para rellenar con tarjetas
                col={"sm": 24, "md": 24, "xl": 24}
            ),
            padding=5,
            margin=25,
            border_radius=15
        )



    for ong in ong_MedioAmbiente:
        # Tarjeta para cada ONG
         tarjeta = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            title=ft.Text(
                                ong["nombre"], color="Black", size=16, weight="bold"),
                            subtitle=ft.Text(
                                ong["descripcion"],
                                text_align="justify", color="Black"
                            ),
                        ),
                        ft.Row(
                            [
                                # Botón para WhatsApp
                                ft.TextButton(
                                    content=ft.Image(
                                        src="whatsapp.jpg", width=32, height=32, tooltip="WhatsApp"),
                                    on_click=lambda e: page.launch_url(
                                        ong["whatsapp"])
                                ),
                                # Botón para Facebook
                                ft.TextButton(
                                    content=ft.Image(
                                        src="facebook.png", width=32, height=32, tooltip="Facebook"),
                                    on_click=lambda e: page.launch_url(
                                        ong["facebook"])
                                ),
                                # Botón para Instagram
                                ft.TextButton(
                                    content=ft.Image(
                                        src="instagram.jpg", width=32, height=32, tooltip="Instagram"),
                                    on_click=lambda e: page.launch_url(
                                        ong["instagram"])
                                )
                            ]
                        ),
                         ft.Row([
                             ft.TextButton(
                            "Más información", on_click=lambda e: page.launch_url(ong["pagina_web"])),
                             ft.TextButton(
                            "Ubicación", on_click=lambda e: page.launch_url(ong[""]),
                            icon = ft.icons.LOCATION_ON),
                            

                        ])
                       
                    ]
                ),
                width=400,
                padding=10,
                bgcolor="white",
                border_radius=10
            ),
            col={"sm": 12, "md": 6, "xl": 4}
        )

         MedioAmbiente.content.controls.append(tarjeta)

    ong_ayuda_social = [
        {
            "nombre": "Ayuda social",
            "descripcion": "Somos un grupo de personas que trabajan en conjunto, con el fin realizar jornadas solidarias para ayudar a los sectores más vulnerables.",
            "whatsapp": "",  
            "facebook": "https://www.facebook.com/share/joeVAXHNJ7rMjQCW/",  
            "instagram": "",  
            "pagina_web": "",
            "Ubicación": "https://www.google.com/maps/place/Capitan+Giachino+2316,+V9410+Ushuaia,+Tierra+del+Fuego/@-54.8098594,-68.3357455,17z/data=!3m1!4b1!4m6!3m5!1s0xbc4c2322a360b407:0x95d01c206e9577f1!8m2!3d-54.8098625!4d-68.3331706!16s%2Fg%2F11s91rpbp6?entry=ttu&g_ep=EgoyMDI0MTAyMy4wIKXMDSoASAFQAw%3D%3D"  
        }
    ] 

    ayuda_social = ft.Container(
        content=ft.ResponsiveRow(
            controls=[],  # Lista vacía para rellenar con tarjetas
            col={"sm": 12, "md": 12, "xl": 12}
        ),
        padding=5,
        margin=25,
        border_radius=15
    )

    for ong in ong_ayuda_social:
        # Tarjeta para cada ONG
            tarjeta = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            title=ft.Text(
                                ong["nombre"], color="Black", size=16, weight="bold"),
                            subtitle=ft.Text(
                                ong["descripcion"],
                                text_align="justify", color="Black"
                            ),
                        ),
                        ft.Row(
                            [
                                # Botón para WhatsApp
                                ft.TextButton(
                                    content=ft.Image(
                                        src="whatsapp.jpg", width=32, height=32, tooltip="WhatsApp"),
                                    on_click=lambda e: page.launch_url(
                                        ong["whatsapp"])
                                ),
                                # Botón para Facebook
                                ft.TextButton(
                                    content=ft.Image(
                                        src="facebook.png", width=32, height=32, tooltip="Facebook"),
                                    on_click=lambda e: page.launch_url(
                                        ong["facebook"])
                                ),
                                # Botón para Instagram
                                ft.TextButton(
                                    content=ft.Image(
                                        src="instagram.jpg", width=32, height=32, tooltip="Instagram"),
                                    on_click=lambda e: page.launch_url(
                                        ong["instagram"])
                                )
                            ]
                        ),
                        ft.Row([
                             ft.TextButton(
                            "Más información", on_click=lambda e: page.launch_url(ong[""])),
                             ft.TextButton(
                            "Ubicación", on_click=lambda e: page.launch_url(ong["Ubicación"]),
                            icon = ft.icons.LOCATION_ON),
                            

                        ])
                       
                    ]
                ),
                width=400,
                padding=10,
                bgcolor="white",
                border_radius=10
            ),
            col={"sm": 12, "md": 6, "xl": 4}
        )

        
            ayuda_social.content.controls.append(tarjeta)



    # AppBar - navegación



    page.horizontal_alignment = page.vertical_alignment = "center"

    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.MUSIC_NOTE)
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    page.appbar = ft.AppBar(
        title=ft.Text("Ushuaia ONG"),
        center_title=True,
        bgcolor=ft.colors.GREEN_300,
        automatically_imply_leading=False,
    )
    
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.BLUE,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.PopupMenuButton(
                                    items=[
                                        ft.PopupMenuItem(text="Inicio",on_click=view_inicio),
                                        ft.PopupMenuItem(),  # divider
                                        ft.PopupMenuItem(text="Educación", on_click=view_educacion),
                                        ft.PopupMenuItem(),  # divider
                                        ft.PopupMenuItem(text="Salud", on_click=view_salud),
                                        ft.PopupMenuItem(),  # divider
                                        ft.PopupMenuItem(text="Animales", on_click=view_animales),
                                        ft.PopupMenuItem(),  # divider
                                        ft.PopupMenuItem(text="Medio Ambiente", on_click=view_medio_ambiente),
                                        ft.PopupMenuItem(),  # divider
                                        ft.PopupMenuItem(text="Ayuda Social", on_click=view_ayuda_social),
                                        ft.PopupMenuItem(),  # divider
                    
                                    ],icon = ft.icons.MENU,
                                    icon_color = "White"
                                    ),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.icons.PAUSE, icon_color=ft.colors.WHITE),
            ]
        ),
    )


    titulo = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "Últimos trabajos realizados",
                    size=40,
                    font_family="Pacifico",
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    color=ft.colors.BLACK87,
                ),
                ft.Text(
                    "Estos son algunos de los últimos trabajos realizados por las ONG de Ushuaia, dedicados a ayudar a la comunidad y mejorar la calidad de vida.",
                    size=16,
                    text_align=ft.TextAlign.CENTER,
                    color=ft.colors.BLACK54,
                )
            ],
        ),
        padding=30,
        border_radius=ft.border_radius.all(15),
    )

    page.add(titulo, carrusel)

    # Actualizar la página
    page.update()


# Ejecutar la aplicación
ft.app(target=main)