from flet import *
from flet_core import *
import flet as ft


def main(page: Page):
    page.title = "Youtube Download"
    page.bgcolor = colors.WHITE
    page.window_title_bar_hidden = True
    page.window_center = True
    page.window_left = 900
    page.window_top = 100
    page.window_always_on_top = True
    page.window_width = 460
    page.window_height = 400
    page.window_resizable = False
    page.padding = 0

    # def window_even(e):
    #     if e.data == "minimize":
    #         print("ya betul")
    #         page.update()

    # page.on_window_event = window_even

    def btn_minimize(e):
        page.window_minimized = True
        page.update()

    def btn_close(e):
        page.window_destroy()
        page.update()

    def btn_no(e):
        confirm_dialog.open = False
        page.update()

    def show_dialog(e):
        page.dialog = confirm_dialog
        confirm_dialog.open = True
        page.update()

    confirm_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm", size=14, weight=FontWeight.W_500),
        content=ft.Text("Do you really want to exit this app?", size=12),
        actions=[
            # ft.ElevatedButton("Yes", height=35, width=60, on_click=btn_close),
            ElevatedButton(
                height=28,
                width=55,
                content=Container(
                    content=Text("Yes", size=12),
                ),
                on_click=btn_close,
            ),
            OutlinedButton(
                height=28,
                width=55,
                content=Container(
                    content=Text(
                        "No",
                        size=12,
                    ),
                ),
                on_click=btn_no,
            )
            # ft.OutlinedButton("No", height=35, width=55, on_click=btn_no),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        actions_padding=padding.only(left=12, right=12, bottom=14),
        content_padding=padding.only(left=12, bottom=10),
        title_padding=padding.only(left=12, top=14, right=12),
        shape=RoundedRectangleBorder(radius=12),
    )

    app_bar = ResponsiveRow(
        spacing=0,
        controls=[
            Column(
                col={"xs": 16, "md": 6},
                controls=[
                    Container(
                        margin=0,
                        padding=0,
                        bgcolor=colors.GREY_200,
                        height=40,
                        content=Row(
                            spacing=0,
                            vertical_alignment=CrossAxisAlignment.CENTER,
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                Row(
                                    spacing=0,
                                    controls=[
                                        Container(
                                            margin=margin.only(right=2),
                                            content=Icon(
                                                name=icons.PLAY_ARROW_ROUNDED,
                                                color=colors.RED,
                                                size=28,
                                            ),
                                        ),
                                        Text(
                                            value="Youtube Download",
                                            color=colors.BLACK,
                                            weight=FontWeight.W_500,
                                            size=16,
                                        ),
                                    ],
                                ),
                                Row(
                                    spacing=0,
                                    alignment=MainAxisAlignment.CENTER,
                                    controls=[
                                        IconButton(
                                            icon=icons.MINIMIZE,
                                            icon_size=18,
                                            on_click=btn_minimize,
                                        ),
                                        IconButton(
                                            icon=icons.CLOSE,
                                            icon_size=18,
                                            on_click=show_dialog,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    )
                ],
            )
        ],
    )

    content = ResponsiveRow(
        controls=[
            Container(
                padding=padding.only(top=44, left=12, right=12),
                content=Column(
                    spacing=0,
                    controls=[
                        Text(
                            "Url Dwonload",
                            color=colors.BLACK,
                            weight=FontWeight.W_500,
                            size=16,
                        ),
                        Container(
                            margin=margin.only(top=0),
                            height=39,
                            content=TextField(
                                text_size=14,
                                color=colors.BLACK,
                                cursor_height=18,
                                border_color=colors.BLUE_300,
                                border=InputBorder.UNDERLINE,
                                hint_text="Enter Url Likn here",
                                on_focus=True,
                                # filled=True,
                            ),
                        ),
                    ],
                ),
            ),
        ],
    )

    page.add(
        Stack(
            controls=[
                content,
                app_bar,
            ]
        )
    )


ft.app(main)
