import flet as ft 

def main(page:ft.Page):
    page.title = "Imagen"
    page.add(ft.Text("Hello, World!"))
    
    page.add(ft.Text(
        value="Hola Mundo",
        size=24,
        color=ft.Colors.BLACK,
        weight=ft.FontWeight.BOLD,
        italic=False,
        text_align=ft.TextAlign.CENTER,
        max_lines=2,
        overflow=ft.TextOverflow.ELLIPSIS
    ))
    
    page.add(ft.Image(
        src="https://picsum.photos/id/1/200/300",
        width=200,
        height=300,
        fit="cover",
        border_radius=ft.BorderRadius.all(10),
        repeat=ft.ImageRepeat.NO_REPEAT,
    ))
    
    page.add(ft.Divider(height=20, thickness=2, color=ft.Colors.GREY_400))
    page.add(ft.Row([
        ft.VerticalDivider(width=10, thickness=2, color=ft.Colors.GREY_400)
    ]))
    
ft.run(main)